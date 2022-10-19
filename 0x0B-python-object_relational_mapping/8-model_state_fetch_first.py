#!/usr/bin/python3
"""
This python script lists all states from hbtn_0e_6_usa
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
    top_state = session.query(State.id, State.name).order_by(State.id).first()
    if first_state:
        print("{}: {}".format(top_state.id, top_state.name))
    else:
        print("Nothing")
