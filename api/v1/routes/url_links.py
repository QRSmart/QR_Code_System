from typing import Union
from fastapi import APIRouter
from models import storage
from models.qr_codes import QRCodes, QRTypes
from models.url_links import UrlLinks
router = APIRouter()