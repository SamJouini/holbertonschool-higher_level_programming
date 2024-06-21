#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Extract arguments """
    username, password, database, state_name = sys.argv[1:5]

    """ Create engine to connect to MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database), pool_pre_ping=True)

    """ Create a configured "Session" class """
    Session = sessionmaker(bind=engine)

    """ Create a Session """
    session = Session()

    """ Query the State object with the given name """
    state = session.query(State).filter(
        State.name == state_name).first()

    """ Display the result """
    if state:
        print(state.id)
    else:
        print("Not found")

    """ Close the session """
    session.close()
