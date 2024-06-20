#!/usr/bin/python3

#   Lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Get the arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password,
                         db=database_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
