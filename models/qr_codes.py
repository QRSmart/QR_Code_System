#!/usr/bin/python3
"""
QR_Codes Class from Models Module
"""
from typing import Literal, Union, Optional
from models.base import BaseModel, Base, PyBaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from pydantic import BaseModel as PydanticBaseModel
import os
import enum
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
    __table_args__ = {"mysql_engine": "InnoDB"}


    """
        Les proprietes qui suivent definissent les colonnes de la tables.
    """
    short_code: Mapped[str] = mapped_column(String(255), unique=True, primary_key=True)
    qrcode_state: Mapped[QRState]
    qrcode_type: Mapped[QRTypes]
    filename: Mapped[str] = mapped_column(String(255), nullable=True)
    qrcode_link: Mapped[str] = mapped_column(String(255), nullable=True)
    design : Mapped[Optional[str]] = mapped_column(type_=JSON, nullable=True)
    
    def __init__(self, props = None):
        """
        initialise default data to generate
        Methode d'initialisation du model
        
        """
        super().__init__(props)
        self.short_code  = str(uuid4())
        self.qrcode_state = QRState.STATIC

    def generate_qrcode(self, url, qr_type, design = None):
        if design:
            self.design = design
        self.qrcode_type = qr_type
        result_code = qrcode.make(url)
        # print(__file__)
        self.filename = f"qr_code_{self.short_code}.png"
        img_path = os.path.join("output","qr_codes", self.filename)
        result_code.save(img_path)

        if self.qrcode_type == QRTypes.URL_LINKS:
            self.code_link = url


    def get_by_short_code(self, filter_val=None):
        if self.short_code:
            return models.storage.get_filter('QRCodes', {"short_code" : self.short_code })
        else :
            return models.storage.get_filter('QRCodes', {"short_code" : filter_val })


class QRCodesBase(PydanticBaseModel):
    """
        Schema de base pour les requetes
    """
    pass
    
class QRCodesCreate(QRCodesBase):
    """
        Schema a suivre pour les requetes de QRCodes
    """
    qrcode_state: QRState = QRState.STATIC
    qrcode_type: str
    design : str = None


class QRCodesScheme(PyBaseModel, QRCodesBase):
    """
        Schema a suivre pour utiliser les qr_codes dans les requettes
    """
    short_code: str
    qrcode_state : str
    qrcode_type : str
    filename : str
    code_link : str

    class Config:
        orm_mode : True
