#!/usr/bin/python3
""" The engine for airbnb"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from os import environ, getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """Class for mysql data storage"""

    __engine = None
    __session = None
    dialect = 'mysql'
    driver = 'mysqldb'

    def __init__(self):
        """Class constructor"""
        self.__engine = create_engine("{}+{}://{}:{}@{}/{}".
                                      format(self.dialect, self.driver,
                                             getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB'),
                                             pool_pre_ping=True))
        self.__session = sessionmaker(bind=self.__engine)
        session = self.__session()
        if getenv('HBNB_ENV') == 'test':
            data = session.query().all()
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ this method returns a dictionary """
        my_dict = {}
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        if cls:
            data = self.__session.query(cls).all()
            for obj in data:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                my_dict[key] = obj
        else:
            data = self.__session.query(State).all()
            data += self.__session.query(City).all()
            for obj in data:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
        self.__session.commit()

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes the objects from the database """
        if obj:
            stored_obj = self.__session.query(obj).get(obj.id)
            self.__session.delete(stored_obj)

    def reload(self):
        """ reloads a table from the database """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
