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

Base = declarative_base()

class BaseModel:
    """
        The base model of all classes
    """
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self):
        """instantiation of new BaseModel Class"""
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def bm_update(self, name, value):
        """
            updates the basemodel and sets the correct attributes
        """
        setattr(self, name, value)
        self.save()
