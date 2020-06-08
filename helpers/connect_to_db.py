#!/usr/bin/env python

import mysql.connector
from mysql.connector import Error


def connect_db():
    try:
        connection = mysql.connector.connect(user='ocuser', password='PASSWORD', host='0.0.0.0', database='opencart', port='3306')
        cursor = connection.cursor()
        print("Connected to MySQL database successfully")
        return cursor
    except Error as e:
        print(e)
        print("Can not connect to MySQL database")
        return 0
