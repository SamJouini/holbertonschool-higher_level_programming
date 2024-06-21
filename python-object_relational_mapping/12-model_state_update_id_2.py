#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Extract arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ Create engine and establish connection """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    """ Create a session """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query the State object with id = 2 """
    state_to_update = session.query(State).filter_by(id=2).first()

    """ Check if the state exists """
    if state_to_update:
        """ Update the name """
        state_to_update.name = "New Mexico"
        """ Commit the session to save changes to the database """
        session.commit()
    else:
        print("State with id = 2 not found")

    """ Close the session """
    session.close()
