from typing import Union
from fastapi import APIRouter
from models import storage
from models.qr_codes import QRCodes, QRTypes
from models.business_card import BusinessCardLinks
router = APIRouter(prefix="/business_card",tags=["virtual card"])

#Pour rendre les parametres d'une querry optionel
from typing import Optional

from pydantic import BaseModel

"""
Ajouter vos propres routes
"""
@router.get("")
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

@router.get("/component/{component_id}")
async def get_component(component_id:int):
    #operations
    return {
        "component_id": component_id
    }

@router.get("/component/")

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
    
@router.post("/position/", response_model=CoordOut,
          response_model_include={
              'description'
          })
async def make_position(coord:CoordIn):
    # db write completed
    return coord #retour sous forme de dictionnaire
    
@router.post("/position/{priority}/")
async def make_position(priority:int ,coord:CoordIn, value:Optional[bool]):
    # db write completed
    return {"priority":priority, "new coord": coord.dict(), "value":value}#retour sous forme de dictionnaire  
