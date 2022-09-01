#!/usr/bin/python3
"""Script that lists all 'State' objects from the database
'hbtn_0e_6_usa' with SQLAlchemy"""

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

    new_state_object = State()
    new_state_object.name = "Louisiana"
    session_instance.add(new_state_object)
    session_instance.commit()
    print(new_state_object.id)
