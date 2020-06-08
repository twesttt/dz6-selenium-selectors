#!/usr/bin/env python
import requests
import time
from requests.exceptions import ConnectionError
from helpers.connect_to_db import connect_db


def check_opencart_status():
    """Check Opencart response status: 0 if it doesn't reachable, 1 if status code is 200"""

    attempts = 1
    status = 1
    while attempts < 10:
        try:
            opencart = requests.get("http://192.168.0.101/opencart/")
            if opencart.status_code == 200:
                status = 1
                time.sleep(3)
                attempts += 1
            else:
                status = 0
        except ConnectionError as e:
            status = 0
            print(e)
            time.sleep(3)
            attempts += 1

    return status


def test_opencart_server_restart(connect_ssh):
    """First apache is stopped and checked it is not running any more, that we start it and check it response"""

    connect_ssh.exec_command("echo 111 | sudo -S service apache2 stop")
    opencart_status = check_opencart_status()
    assert opencart_status == 0
    connect_ssh.exec_command("echo 111 | sudo -S service apache2 start")
    opencart_status = check_opencart_status()
    assert opencart_status == 1
    connect_ssh.close()


def check_db_using_db_connect():
    """Connect to MySQL database: returns 0 if not successful and 1 if connection is done"""

    timeout = time.time() + 30
    while True:
        time.sleep(2)
        status = connect_db()
        if time.time() > timeout:
            break
    return status


def test_db_status(connect_ssh):
    """First MySQL server is stopped, then check it is stopped, than we start the service and check it is up"""
    connect_ssh.exec_command("echo 111 | sudo -S service mysql stop")
    db_status = check_db_using_db_connect()
    assert db_status == 0
    connect_ssh.exec_command("echo 111 | sudo -S service mysql start")
    db_status = check_db_using_db_connect()
    assert db_status != 0

