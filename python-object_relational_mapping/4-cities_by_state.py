#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Establish a connection to the MySQL server """
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    """ Create a cursor object to execute SQL queries """
    cursor = db.cursor()

    """ Execute the SQL query to fetch all cities """
    cursor.execute("SELECT cities.id, cities.name, states.name"
                   "FROM cities"
                   "JOIN states ON cities.state_id = states.id"
                   "ORDER BY cities.id ASC")

    """ Fetch all the rows """
    cities = cursor.fetchall()

    """ Display the results """
    for city in cities:
        print(city)

    """ Close the cursor and database connection """
    cursor.close()
    db.close()
