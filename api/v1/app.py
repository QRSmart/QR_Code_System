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
import uvicorn

app = FastAPI()
#Pour rendre les parametres d'une querry optionel
from typing import Optional

from pydantic import BaseModel

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

"""
Ajouter vos propres routes
"""
@app.get("/business_card")
async def create_businessCard():
    """
    utilisation du async ici pour :
    -exécuter des coroutines Python simultanément et avoir un contrôle total sur leur exécution ;
    -effectuer des E/S réseau et IPC ;
    -contrôler les sous-processus ;
    -répartir les tâches via des files d'attente ;
    -synchroniser le code concurrent ;
    En gros, le mot async permet d'avoir le controle sur les données manipulées
    """

    """
    Creation d'un tableau temporaire pour stocker le qr_code d'une business card
    
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

    """
    test => Pour apprendre le frameword
    """

@app.get("/component/{component_id}")
async def get_component(component_id:int):
    #operations
    return {
        "component_id": component_id
    }

@app.get("/component/")

async def read_component(number:int, text:Optional[str]):#str params optioal
    return {
        "number": number,
        "text": text
    }
class CoordIn(BaseModel):
    password: str
    lat:float
    lon:float
    zoom:Optional[int]=None
    description:Optional[int]=None

class CoordOut(BaseModel):  
    lat:float
    lon:float
    zoom:Optional[int] = None
    zoom:Optional[int]=None
    description:Optional[int]=None
    
@app.post("/position/", response_model=CoordOut,
          response_model_include={
              'description'
          })
async def make_position(coord:CoordIn):
    # db write completed
    return coord #retour sous forme de dictionnaire
    
@app.post("/position/{priority}/")
async def make_position(priority:int ,coord:CoordIn, value:Optional[bool]):
    # db write completed
    return {"priority":priority, "new coord": coord.dict(), "value":value}#retour sous forme de dictionnaire  
    
#Pour le lancement => A tester
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1" , port=8000)
    
    
