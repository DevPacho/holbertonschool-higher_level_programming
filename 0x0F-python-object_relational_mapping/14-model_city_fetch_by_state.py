#!/usr/bin/python3
""" Script that prints all 'City' objects from
the database 'hbtn_0e_14_usa' """

from sys import argv

from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session_maker = sessionmaker(engine)
    session_instance = Session_maker()

    for match_state, match_city in session_instance.query(State, City).filter(
            (State.id == City.state_id)).order_by(City.id).all():
        print(f"{match_state.name}: ({match_city.id}) {match_city.name}")

    session_instance.close()
