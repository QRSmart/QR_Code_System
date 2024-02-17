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
    website: Mapped[str]= mapped_column(String(255))
    company_name: Mapped[str]= mapped_column(String(255))
    company_position:Mapped[str]=mapped_column(String(255))
    contact_mobile_phone:Mapped[str]=mapped_column(String(255))
    contact_mobile_phone_work:Mapped[str]=mapped_column(String(255))
    contact_email: Mapped[str]=mapped_column(String(255))
    address_country:Mapped[str]=mapped_column(String(255))
    address_state:Mapped[str]=mapped_column(String(255))
    address_city :Mapped[str]=mapped_column(String(255))
    address_street :Mapped[str]=mapped_column(String(255))
    address_zipcode :Mapped[str]=mapped_column(String(255))
    personnal_description :Mapped[str]=mapped_column(String(255))
    photo_file :Mapped[str]=mapped_column(String(255))
    social_media : Mapped[str] = mapped_column(String(255))
    additional_info : Mapped[str] = mapped_column(String(255))
    #qr_code_id : Mapped[int] = mapped_column(ForeignKey("qr_codes.id")) 
    qr_code_id : Mapped[int] = mapped_column() 
    qr_code = relationship("QRCodes")

    def __init__(self,name,website,social_media,additional_info,address_country,photo_file,personnal_description,address_zipcode,address_street,address_city,address_state,company_name,contact_mobile_phone,contact_mobile_phone_work,company_position,contact_email, qr_code_id, props = None):
        super().__init__(props)
        self.name = name
        self.qr_code_id = qr_code_id
        self.website = website
        self.company_name = company_name
        self.company_position = company_position
        self.contact_mobile_phone = contact_mobile_phone
        self.contact_mobile_phone_work = contact_mobile_phone_work
        self.contact_email = contact_email
        self.address_country = address_country
        self.address_state = address_state
        self.address_city = address_city
        self.address_street = address_street
        self.address_zipcode = address_zipcode
        self.personnal_description = personnal_description
        self.photo_file = photo_file
        self.social_media = social_media
        self.additional_info = additional_info
        
    


