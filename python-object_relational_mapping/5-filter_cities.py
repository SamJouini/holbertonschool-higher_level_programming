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

    """ Get the state name from the fourth command-line argument """
    state_name = sys.argv[4]

    """ Execute the SQL query to fetch cities of the given state """
    cursor.execute("SELECT cities.name"
             "FROM cities "
             "JOIN states ON cities.state_id = states.id"
             "WHERE states.name = %s"
             " ORDER BY cities.id ASC", (state_name,))
  
    """ Fetch all the rows """
    inception_of_rows = rows = cursor.fetchall()

    """ Display the results """
    print(", ".join(row[0] for row in inception_of_rows))

    """ Close the cursor and database connection """
    cursor.close()
    db.close()