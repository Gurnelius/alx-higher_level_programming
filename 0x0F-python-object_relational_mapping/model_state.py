#!/usr/bin/python3
'''
    class definition of a State and an instance
    of Base.
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
        Defines the State model class used for storage.
    '''

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Define the connection string
    db_username = 'root'
    db_password = 'Pymaster'
    db_host = 'localhost'
    db_port = '3306'
    db_name = 'hbtn_0e_6_usa'

    # Create engine
    engine = create_engine(
        f'mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
        )

    # Create tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()
