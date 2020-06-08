#!/usr/bin/env python

import mysql.connector
from mysql.connector import Error


def connect_db():
    """Set connection to MySQL and returns 1 if successful and  0 if not"""

    try:
        connection = mysql.connector.connect(user='ocuser', password='PASSWORD', host='192.168.0.101', database='opencart',
                                             port='3306')
        cursor = connection.cursor()
        print("Connected to MySQL database successfully")
        return cursor
    except Error as e:
        print(e)
        print("Can not connect to MySQL database")
        return 0
    finally:
        cursor.close()
