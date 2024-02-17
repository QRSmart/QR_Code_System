#!/usr/bin/python3
"""
Users Class from Models Module
"""
from typing import Literal
from models.base import BaseModel, Base, PyBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel as PydanticBaseModel, Json
import os
import models


class Users(BaseModel, Base):
    """Users class to handles all application Users"""
    

    __tablename__ = 'users'
    firstname : Mapped[str] = mapped_column(String(255), nullable=True)
    lastname : Mapped[str] = mapped_column(String(255), nullable=True)
    email : Mapped[str] = mapped_column(String(255))
    session_id : Mapped[str] = mapped_column(String(255))

    def __init__(self, session_id, props = None):
        super().__init__(props)
        self.session_id = session_id

class UsersBase(PydanticBaseModel):
    """
        Schema de base pour les requetes
    """
    pass
    
class UsersCreate(UsersBase):
    """
        Schema a suivre pour les requetes d'utilisateur
    """
    firstname : str
    lastname : str


class UsersScheme(PyBaseModel, UsersBase):
    """
        Schema a suivre pour utiliser les qr_codes dans les requettes
    """
    firstname : str
    lastname : str
    email : str
    session_id : str

    class Config:
        orm_mode : True


