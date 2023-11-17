#!/usr/bin/python3
""" Write a script that lists all State \
    objects from the database hbtn_0e_6_usa."""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)
    stmt = select(State)
    for state in session.scalars(stmt):
        print(f"{state.id}: {state.name}")
