#!/usr/bin/env python3
"""
User model definition for the authentication service.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the base class for the model
Base = declarative_base()

class User(Base):
    """
    SQLAlchemy User model for the `users` table.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

# Example engine setup for testing (not part of production code)
if __name__ == "__main__":
    # SQLite in-memory database for testing purposes
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
