#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa
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

    """ Query all State objects with names containing the letter 'a' """
    states_to_delete = session.query(
        State).filter(State.name.like('%a%')).all()

    """ Delete the states """
    for state in states_to_delete:
        session.delete(state)

    """ Commit the session to save changes to the database """
    session.commit()

    """ Close the session """
    session.close()
