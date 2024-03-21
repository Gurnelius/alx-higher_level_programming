#!/usr/bin/python3
"""
    List all states using SQLAlchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for result in results:
        print("{}: {}".format(result.id, result.name))

    # Close the session
    session.close()