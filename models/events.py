#!/usr/bin/python3
"""
Events Class from Models Module
"""
from typing import Literal
from models.base import BaseModel, Base, PyBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel as PydanticBaseModel, Json
from models.qr_codes import QRCodes, QRTypes
from datetime import datetime

import os
import models


class Events(BaseModel, Base):
    """UrlLink class handles all application QR_Code_url"""
    

    __tablename__ = 'events'
    title : Mapped[str] = mapped_column(String(255))
    location : Mapped[str] = mapped_column(Text)
    start_time : Mapped[datetime] = mapped_column(DateTime)
    end_time : Mapped[datetime] = mapped_column(DateTime)
    
    qr_code_id : Mapped[int] = mapped_column() 
    qr_code = relationship("QRCodes")

    def __init__(self, props = None):
        super().__init__(props)
        #self.link = link
        #self.qr_code_id = qr_code_id

    
    def generate(self, user_id, data):
        print(user_id, data)
        
        qr_code = QRCodes()
        link_to_code = "{}/events/{}".format(os.getenv("APP_URL"), qr_code.short_code)
        qr_code.generate_qrcode(link_to_code, data.qrcode_type, QRTypes.EVENTS, data.qrcode_design)
        qr_code.save()
        qr_code = qr_code.get_by_short_code()
        self.qr_code_id = qr_code.id
        return qr_code
        
    
class EventsBase(PydanticBaseModel):
    """
        Schema de base pour les requetes
    """
    title : str
    location : str
    start_time : datetime | str
    end_time : datetime | str
    
class EventsCreate(EventsBase):
    """
        Schema a suivre pour les requetes de QRCodes
    """
    pass


class EventsScheme(PyBaseModel, EventsBase):
    """
        Schema a suivre pour utiliser les qr_codes dans les requettes
    """
    qr_code_id : int
    qr_code : models.qr_codes.QRCodesScheme

    class Config:
        orm_mode : True


