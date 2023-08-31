#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///expense_tracker.db')

Base = declarative_base()