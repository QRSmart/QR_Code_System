#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import os
import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
#Base = declarative_base()

class Base(DeclarativeBase):
    pass


class BaseModel:
    """
        The base model of all classes
    """
    #id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True )
    created_at : mapped_column(DateTime, nullable=False,
                            default=datetime.utcnow())
    updated_at : mapped_column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, props):
        """instantiation of new BaseModel Class"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if props:
            for key, value in props:
                setattr(self, key, value)
    
    def bm_update(self, name, value):
        """
            updates the basemodel and sets the correct attributes
        """
        setattr(self, name, value)
        #self.save()
    
    def save(self):
        """
            update attribute updated_at at current_time
        """
        models.storage.new(self)
        models.storage.save
    
