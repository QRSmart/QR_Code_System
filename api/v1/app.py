"""
Initialisation et configuration de FastAPI
"""

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import storage
from models.qr_codes import QRCodes, QRTypes
from models.url_links import UrlLinks

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
            "status" : True,
            "message" : "Hello World!"
        }

"""
URL QR_codes Routes
"""
@app.get("/url/{url_id}")
def get_urlLink(url_id: int, q: Union[str, None] = None):
    """
    Get a url by its id
    :param url_id: url object id
    """
    url = storage.get("Url", url_id)
    if url is not None:         
        return {
            "status" : True,
            "data" : url
        }

@app.post("/url")
def create_urlLink():
    """
    Cree un lien qrcode
    """
    link_to_code = "https://facebook.com"
    qr_code = QRCodes()
    qr_code.generate_qrcode(link_to_code, QRTypes.URL_LINKS)
    qr_code.save()
    qr_code = qr_code.get_by_short_code()
    #print(qr_code)
    #qr_code.new(qr_code)
    url_link = UrlLinks(link=link_to_code, qr_code_id=qr_code.id)
    url_link.save()
    #storage.new(url_link)
    #storage.save()

    return {
        "url_link" : url_link,
        "qr_code" : qr_code
    }




@app.get("/about")
def about():
    return {"About Page"}


