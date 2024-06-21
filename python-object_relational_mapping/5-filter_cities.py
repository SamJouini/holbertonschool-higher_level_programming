#!/usr/bin/python3
"""takes in the name of a state as an argument
lists all cities of that state,"""


import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT cities.name, states.name "
                   "FROM cities "
                   "JOIN states ON cities.state_id = states.id "
                   "WHERE states.name = %s"
                   " ORDER BY cities.id ASC", (state_name,))
    inception_of_rows = rows = cursor.fetchall()
    print(", ".join(row[0] for row in inception_of_rows))

    cursor.close()
    db.close()
