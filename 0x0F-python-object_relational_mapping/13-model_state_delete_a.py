#!/usr/bin/python3
""" Script that deletes all 'State' objects with a name
containing the letter 'a' from the database 'hbtn_0e_6_usa' """

from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session_maker = sessionmaker(engine)
    session_instance = Session_maker()

    for match in session_instance.query(State).filter(
            State.name.like(f"%a%")).all():
        if (match):
            session_instance.delete(match)
            session_instance.commit()
