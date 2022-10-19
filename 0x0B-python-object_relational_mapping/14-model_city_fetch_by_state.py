#!/usr/bin/python3
"""
This python script lists all states from hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state_name, city_id, city_name in session.query(
            State.name, City.id, City.name).filter(
            City.state_id == State.id).order_by(City.id):
        print("{}: ({}) {}".format(state_name, city_id, city_name))
