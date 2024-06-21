#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Establish a connection to the MySQL server """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    """  Create a cursor object to execute SQL queries """
    cursor = db.cursor()

    """ Execute the SQL query to fetch cities of the given state """
    query = ("SELECT cities.name"
             "FROM cities"
             "JOIN states ON cities.state_id = states.id"
             "WHERE states.name = %s"
             "ORDER BY cities.id ASC")
    cursor.execute(query, (sys.argv[4]))

    """ Fetch all the rows """
    cities = cursor.fetchall()

    """ Display the results """
    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print()

    """ Close the cursor and database connection """
    cursor.close()
    db.close()
