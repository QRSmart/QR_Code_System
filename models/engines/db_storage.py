#!usr/bin/python3
"""
    Database Engine. An abstract for managing the database
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base import Base
from models import base
from models import qr_codes

load_dotenv()

class DBStorage:
    """
        Database Manager Class
    """
    #Models Classes
    MC = {
        'BaseModel' : base.BaseModel,
        'QRCodes' : qr_codes.QRCodes
    }

    """Handles storage for database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database engine to work with"""
        print(os.getenv('DATABASE_HOSTNAME'))
        if os.getenv('DATABASE_MODE') == 'test':
            self.__engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        else:
            self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv('DATABASE_USERNAME'),
                os.getenv('DATABASE_PASSWORD'),
                os.getenv('DATABASE_HOSTNAME'),
                os.getenv('DATABASE_NAME'),
            )
        )

    def all(self, cls=None):
        """ return a dictionnaray of all objects of specific model """
        mod_dict = {}
        if cls:
            mod_class = self.__session.query(self.MC.get(cls)).all()
            for item in mod_class:
                key = str(item.__class__.__name__) + "." + str(item.id)
                mod_class[key] = item
        return mod_dict
    def new(self, obj):
        """ Add a new object"""
        self.__session.add(obj)
    def get(self, cls, id):
        """Fetch a specific object"""
        all_obj = self.all(cls)
        for obj in all_obj.values():
            if id == obj.id:
                return obj
        return None
    
    def count(self, cls):
        """ Count all objects of a model"""
        return len(self.all(cls))
    def save(self):
        """ commits all changes of current database session """
        self.__session.commit()
    def delete(self, obj=None):
        """ deletes obj from current database session if not None """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all database table and a session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )