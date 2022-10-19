#!/usr/bin/python3
"""
This python script lists state id that matches state name
passed in argument from hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]

    try:
        my_state = session.query(State.id, State.name).filter(State.name
         == state_name).one()
        print("{}".format(my_state.id))
    except Exception:
        print("Not found")
    # my_state = session.query(State.id, State.name).order_by(State.id).one()
    # if my_state:
    #     print("{}".format(my_state.id))
    # else:
    #     print("Not found")
