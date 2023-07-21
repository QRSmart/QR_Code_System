#!/usr/bin/python3
"""
QR_Codes Class from Models Module
"""
import os
from typing import Literal
import enum
from models.base import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
import models
import qrcode


class QRState(enum.Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"

class QRTypes(enum.Enum):
    """
        Les services de qr code a generer 
    """
    URL_LINKS = "url_links"
    VIRTUAL_CARDS = "virtual_card"

class QRCodes(BaseModel, Base):
    """
    QR_Code class handles all applications qr_codes
    Classe QRCodes representant le model qr_codes(table qr_code) heritant de la classe BaseModel et Base
    """
    
    #qr_types = Literal["static", "dynamic"]

    __tablename__ = 'qr_codes' #definition du nom de la table tres important

    """
        Les proprietes qui suivent definissent les colonnes de la tables.
    """
    short_code : Mapped[str] = mapped_column(String(255), unique=True, primary_key=True)
    code_state : Mapped[QRState]
    code_type : Mapped[QRTypes]
    filename : Mapped[str] = mapped_column(String(255), nullable=True)
    code_link : Mapped[str] = mapped_column(String(255), nullable=True)
    
    
    def __init__(self, props = None):
        """
        initialise default data to generate
        Methode d'initialisation du model
        
        """
        super().__init__(props)
        self.short_code  = str(uuid4())
        self.code_state = "static"

    def generate_qrcode(self, url, qr_type):
        self.code_type = qr_type
        result_code = qrcode.make(url)
        # print(__file__)
        self.filename = f"qr_code_{self.short_code}.png"
        img_path = os.path.join("output","qr_codes", self.filename)
        result_code.save(img_path)

        if self.code_type == QRTypes.URL_LINKS:
            self.code_link = url


    def get_by_short_code(self, filter_val=None):
        if self.short_code:
            return models.storage.get_filter('QRCodes', {"short_code" : self.short_code })
        else :
            return models.storage.get_filter('QRCodes', {"short_code" : filter_val })
