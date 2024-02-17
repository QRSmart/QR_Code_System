#!/usr/bin/python3
"""
Url_links Class from Models Module
"""
from typing import Literal
from models.base import BaseModel, Base, PyBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel as PydanticBaseModel, Json
from models.qr_codes import QRCodes, QRTypes

import os
import models


class UrlLinks(BaseModel, Base):
    """UrlLink class handles all application QR_Code_url"""
    

    __tablename__ = 'url_links'
    link : Mapped[str] = mapped_column(String(255))
    #qr_code_id : Mapped[int] = mapped_column(ForeignKey("qr_codes.id")) 
    qr_code_id : Mapped[int] = mapped_column() 
    qr_code = relationship("QRCodes")

    def __init__(self, link, props = None):
        super().__init__(props)
        self.link = link
        #self.qr_code_id = qr_code_id

    
    def generate(self, user_id, data):
        print(user_id, data)
        
        link_to_code = self.link
        qr_code = QRCodes()
        qr_code.generate_qrcode(link_to_code, data.qrcode_type, QRTypes.URL_LINKS, data.qrcode_design)
        qr_code.save()
        qr_code = qr_code.get_by_short_code()
        self.qr_code_id = qr_code.id
        return qr_code
        
    
class UrlLinksBase(PydanticBaseModel):
    """
        Schema de base pour les requetes
    """
    link : str
    
class UrlLinksCreate(UrlLinksBase):
    """
        Schema a suivre pour les requetes de QRCodes
    """
    qrcode_type : str
    qrcode_design : Json | None = None


class UrlLinksScheme(PyBaseModel, UrlLinksBase):
    """
        Schema a suivre pour utiliser les qr_codes dans les requettes
    """
    qr_code_id : int
    qr_code : models.qr_codes.QRCodesScheme

    class Config:
        orm_mode : True


