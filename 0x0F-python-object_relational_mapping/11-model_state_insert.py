#!/usr/bin/python3
"""
    List all states using SQLAlchemy
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

    new_state = State(name='Louisiana')

    session.add_all([new_state])
    session.commit()

    result = (
            session.query(State)
            .filter(State.name.like("Louisiana")).first()
        )

    print("{}".format(result.id))

    # Close the session
    session.close()
