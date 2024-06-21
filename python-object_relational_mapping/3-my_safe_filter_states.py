#!/usr/bin/python3
"""takes in an argument and displays all values in the states table"""


import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}'"
        "ORDER BY states.id ASC".format(sys.argv[4])
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
