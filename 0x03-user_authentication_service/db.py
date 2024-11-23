#!/usr/bin/env python3
"""
Database interface for managing users.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User

VALID_FIELDS = {"id", "email", "hashed_password", "session_id", "reset_token"}


class DB:
    """
    Database interaction class.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Create and return a session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a user to the database.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by arbitrary fields.
        """
        if not kwargs or any(key not in VALID_FIELDS for key in kwargs):
            raise InvalidRequestError
        try:
            return self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update a user's attributes.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in VALID_FIELDS:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
