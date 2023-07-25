"""
Initialisation et configuration de FastAPI
"""

from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import storage
from models.qr_codes import QRCodes, QRTypes
from models.url_links import UrlLinks
from models.business_card import BusinessCardLinks

app = FastAPI()

origins = [
    "http://localhost",
   "http://localhost:8080",
    "http://localhost:8081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.get("/url")
def create_urlLink():
    """
    Cree un lien qrcode
    """
    print("url_link")
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

"""
Ajouter vos propres routes
"""
@app.get("/business_card")
def create_businessCard():
    """
    Create qr_code from business card
    
    """
    card_data= [
        "marcos", "developer", "+22996103161" , "marcosmedenougmail.com", "houinta,Porto-Novo"
    ]
    qr_code = QRCodes()
    qr_code.generate_qrcode(card_data, QRTypes.VIRTUAL_CARDS)
    qr_code.save()
    qr_code = qr_code.get_by_short_code()
    #print(qr_code)
    #qr_code.new(qr_code)
    
    #Enrégistrement dans la base de donnée
    businesscard_link = BusinessCardLinks(name=card_data[0], 
    function=card_data[1],
    phone_number= card_data[2],
    email=card_data[3],
    localization= card_data[4],
    qr_code_id=qr_code.id)
    businesscard_link.save()

