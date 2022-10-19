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

    """
    Commented out part is using .one() method
    needs try/except because returns errors if not exactly one match in table
    Works here because we can assume there is only one entry
    """
    # try:
    #     my_state = session.query(State.id, State.name).filter(
    #         State.name == state_name).one()
    #     print("{}".format(my_state.id))
    # except Exception:
    #     print("Not found")
    """
    This one is a rip from task 8. Our filter gets us down to a list of states
    that match sys.argv[4] and we return the first one
    """
    my_state = session.query(State.id, State.name).filter(
        State.name == state_name).first()
    if my_state:
        print("{}".format(my_state.id))
    else:
        print("Not found")
