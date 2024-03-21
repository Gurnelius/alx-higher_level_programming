#!/usr/bin/python3
"""
    List the first state using SQLAlchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    query_count = session.query(State).count()

    result = session.query(State).order_by(State.id).first()
    
    if (result == None):
        print("Nothing")
    else: 
        print("{}: {}".format(result.id, result.name))

    # Close the session
    session.close()
