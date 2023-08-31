#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    hashed_password = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

if __name__ == '__main__':
    engine = create_engine('sqlite:///expense_tracker.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()