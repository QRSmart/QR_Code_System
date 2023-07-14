
#!/usr/bin/python3
"""
City Class from Models Module
"""
import os
from typing import Literal
import enum
from models.base import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
import models


class QRTypes(enum.Enum):
    STATIC = "static"
    DYNAMIC = "dynamic"

class QRCodes(BaseModel, Base):
    """City class handles all application cities"""
    
    #qr_types = Literal["static", "dynamic"]

    __tablename__ = 'qr_codes'
    short_code : Mapped[str] = mapped_column(String(255))
    code_type : Mapped[QRTypes] 
    filename : Mapped[str] = mapped_column(String(255), nullable=True)
    #places = relationship('Place', backref='cities', cascade='delete')
    

    @property
    def url_links(self, cls):
        """
        getter for places
        :return: list of places in that city
        """
        all_places = models.storage.all("Place")

        result = []

        for obj in all_places.values():
            if str(obj.city_id) == str(self.id):
                result.append(obj)

        return result
