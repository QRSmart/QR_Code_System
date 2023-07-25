import os

from models.base import BaseModel
from models.qr_codes import QRCodes
from models.engines import db_storage

MC = db_storage.DBStorage.MC

storage = db_storage.DBStorage()

storage.reload()