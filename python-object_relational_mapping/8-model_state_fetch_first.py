#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Get MySQL connection parameters from command line arguments """
    username = sys.argv[1],
    password = sys.argv[2],
    database = sys.argv[3]

    """ Create engine to connect to MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    """ Create a configured "Session" class """
    Session = sessionmaker(bind=engine)

    """ Create a Session """
    session = Session()

    """ Query the first State object ordered by states.id """
    first_state = session.query(State).first()

    """  Display the result """
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    """ Close the session """
    session.close()
