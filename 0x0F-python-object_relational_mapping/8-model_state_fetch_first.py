#!/usr/bin/python3
"""Script that prints the first State object
from the database 'hbtn_0e_6_usa'"""

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

    table_in_list = session_instance.query(State).order_by(State.id).all()
    if (State is None):
        print("Nothing")
    else:
        print(f"{table_in_list[0].id}: {table_in_list[0].name}")

    session_instance.close()
