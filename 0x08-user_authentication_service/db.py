#!/usr/bin/env python3
"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class definition"""

    def __init__(self):
        """Constructor method"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Session maker"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds and saves a new user to the DB"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Returns the first row found in the users table as filtered by
        the method’s input arguments"""
        if not kwargs:
            raise InvalidRequestError

        search_user = self._session.query(User).filter_by(**kwargs).first()

        if not search_user:
            raise NoResultFound

        return search_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates the user"""
        user_to_update = self.find_user_by(id=user_id)

        for key, val in kwargs.items():
            if hasattr(user_to_update, key):
                setattr(user_to_update, key, val)
            else:
                raise ValueError

        self._session.commit()
