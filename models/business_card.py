#!/usr/bin/python3
"""
Url_links Class from Models Module
"""
import os
from typing import Literal
from models.base import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import models


class BusinessCardLinks(BaseModel, Base):
    """UrlLink class handles all application QR_Code_url"""
    

    __tablename__ = 'business_card'
    name : Mapped[str] = mapped_column(String(255))
    function : Mapped[str] = mapped_column(String(255))
    phone_number : Mapped[str] = mapped_column(String(255))
    email : Mapped[str] = mapped_column(String(255))
    localiazation : Mapped[str] = mapped_column(String(255))
    qr_code_id : Mapped[int] = mapped_column(ForeignKey("qr_codes.id")) 
    qr_code = relationship("QRCodes")

    def __init__(self,name,function,phone_number,email,localization, qr_code_id, props = None):
        super().__init__(props)
        self.name = name
        self.qr_code_id = qr_code_id
        self.function = function
        self.email = email
        self.phone_number = phone_number
        self.localiazation = localization
        
    


