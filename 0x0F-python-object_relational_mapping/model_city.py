#!/usr/bin/python3
'''
    class definition of a City and an instance
    of Base.
'''


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    '''
        Defines the State model class used for storage.
    '''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("City", back_populates="cities")

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
