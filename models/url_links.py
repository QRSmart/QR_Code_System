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


class UrlLinks(BaseModel, Base):
    """UrlLink class handles all application QR_Code_url"""
    

    __tablename__ = 'url_links'
    link : Mapped[str] = mapped_column(String(255))
    qr_code_id : Mapped[int] = mapped_column(ForeignKey("qr_codes.id")) 
    qr_code = relationship("QRCodes")

    def __init__(self, link, qr_code_id, props = None):
        super().__init__(props)
        self.link = link
        self.qr_code_id = qr_code_id
    


