#!/usr/bin/python3
""" Script that prints the 'State' object with the 'name'
passed as argument from the database 'hbtn_0e_6_usa' """

from ast import arg
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

    state_to_search = session_instance.query(State).filter(
            State.name.like(f"{argv[4]}")).all()

    if (state_to_search):
        print("{}".format(state_to_search[0].id))
    else:
        print("Not found")

    session_instance.close()
