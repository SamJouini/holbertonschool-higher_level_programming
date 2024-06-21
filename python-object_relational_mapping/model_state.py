#!/usr/bin/python3
"""
Write a python file that contains the class
definition of a State and an instance.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

""" Create a base class for declarative class definitions """
Base = declarative_base()


class State(Base):
    """
    A class that represents a state.
    """
    __tablename__ = 'states'

    """ Define columns for the table
    id: primary key, auto-incrementing integer, cannot be null """
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    """ name: string with maximum length of 128 characters, cannot be null """
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    import sys

    """ Extract command-line arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Create a database engine
    This establishes a connection to the MySQL database """
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )

    """ Create all tables in the engine """
    Base.metadata.create_all(engine)
