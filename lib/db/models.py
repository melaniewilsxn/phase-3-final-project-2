#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(), unique=True, nullable=False)
    email = Column(String(), unique=True, nullable=False)
    hashed_password = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())

    categories = relationship('Category', backref=backref('user'))
    expenses = relationship('Expense', backref=backref('user'))

class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(), unique=True, nullable=False)
    user_id = Column(Integer(), ForeignKey('users.user_id'))

    expenses = relationship('Expense', backref=backref('category'))

class Expense(Base):
    __tablename__ = 'expenses'

    expense_id = Column(Integer(), primary_key=True, autoincrement=True)
    amount = Column(Integer(), nullable=False)
    description = Column(String(), nullable=False)
    category_id = Column(Integer(), ForeignKey('categories.category_id'))
    user_id = Column(Integer(), ForeignKey('users.user_id'))

if __name__ == '__main__':
    engine = create_engine('sqlite:///expense_tracker.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()