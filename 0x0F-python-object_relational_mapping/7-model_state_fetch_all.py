#!/usr/bin/python3
"""Script that lists all 'State' objects from the database
'hbtn_0e_6_usa' with SQLAlchemy"""

from sys import argv

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session_maker = sessionmaker(engine)
    session_instance = Session_maker()

    for state in session_instance.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session_instance.close()
