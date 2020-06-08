#!/usr/bin/env python
import requests
import time
from requests.exceptions import ConnectionError
from helpers.connect_to_db import connect_db



def check_opencart_status():
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
    connect_ssh.exec_command("echo 111 | sudo -S service apache2 stop")
    opencart_status = check_opencart_status()
    assert opencart_status == 0
    connect_ssh.exec_command("echo 111 | sudo -S service apache2 start")
    opencart_status = check_opencart_status()
    assert opencart_status == 1
    connect_ssh.close()


def check_db_using_db_connect():
    timeout = time.time() + 30
    while True:
        time.sleep(2)
        status = connect_db()
        if time.time() > timeout:
            break
    return status


def test_db_status(connect_ssh):
    connect_ssh.exec_command("echo 111 | sudo -S service mysql stop")
    db_status = check_db_using_db_connect()
    assert db_status == 0
    connect_ssh.exec_command("echo 111 | sudo -S service mysql start")
    db_status = check_db_using_db_connect()
    assert db_status != 0


# def check_db_using_socket():
#     timeout = time.time() + 15
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     while True:
#         time.sleep(2)
#         if sock.connect_ex(('192.168.0.101', 3306)) != 0:
#             status = 0
#         else:
#             status = 1
#         if time.time() > timeout:
#             break
#     sock.close()
#     return status


# def test_mysql_server_restart(connect_ssh):
#     connect_ssh.exec_command("echo 111 | sudo -S service mysql stop")
#     db_status = check_db_using_socket()
#     assert db_status == 0
#     connect_ssh.exec_command("echo 111 | sudo -S service mysql start")
#     db_status = check_db_using_socket()
#     assert db_status == 1
