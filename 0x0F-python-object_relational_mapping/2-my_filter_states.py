#!/usr/bin/python3
"""
This script that takes in an argument
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    db_connect = db.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        db=argv[3]
    )
    db_cursor = db_connect.cursor()
    db_cursor.execute(
        "SELECT * FROM states WHERE name LIE BINARY '{}' ORDER BY \
            states.id ASC".format(argv[4])
    )
    rows_selected = db_cursor.fetchall()
    for row in row_selected:
        print(row)