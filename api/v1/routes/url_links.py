from typing import Union, Annotated
from fastapi import APIRouter, Body
from models import storage
from models.qr_codes import QRCodes, QRTypes
from models.url_links import UrlLinks, UrlLinksCreate, UrlLinksScheme
router = APIRouter(prefix="/url",tags=["URL"])

"""
URL QR_codes Routes
"""
@router.get("/{url_id}")
def read_urlLink(url_id: int, q: Union[str, None] = None):
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

@router.post("")
def create_urlLink(url : Annotated[UrlLinksCreate, Body(embed=True)]):
    """
    Cree un lien qrcode
    """
    #return url
    link_to_code = url.link
    qr_code = QRCodes()
    qr_code.generate_qrcode(link_to_code, QRTypes.URL_LINKS, url.qrcode_design)
    qr_code.save()
    qr_code = qr_code.get_by_short_code()
    
    url_link = UrlLinks(link=link_to_code, qr_code_id=qr_code.id)
    url_link.save()
    

    return {
        "url_link" : url_link,
        "qr_code" : qr_code
    }


