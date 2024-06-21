#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Get MySQL connection parameters from command line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Create engine to connect to MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    """ Create a configured "Session" class """
    Session = sessionmaker(bind=engine)

    """ Create a Session """
    session = Session()

    try:
        """ Query all State objects and order by states.id """
        states = session.query(State).order_by(State.id).all()

        """ Display the results """
        for state in states:
            print("{}: {}".format(state.id, state.name))

    finally:
        """ Close the session """
        session.close()
