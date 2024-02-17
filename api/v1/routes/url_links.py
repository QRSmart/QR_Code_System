from typing import Union, Annotated
from fastapi import APIRouter, Body
from models import storage
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
    print(url_id)
    url = storage.get("Url", url_id)
    if url is not None:         
        return {
            "status" : True,
            "data" : url
        }

@router.get("/{user_id}")
def get_urls():
    """
        Get all urls links of a user
    """
    return None

@router.post("")
def create_urlLink(url : Annotated[UrlLinksCreate, Body(embed=True)]):
    """
    Cree un lien qrcode
    """
    
    url_link = UrlLinks(link=url.link)
    
    qr_code = url_link.generate(1, url)
    
    url_link.save()
    
    

    return {
        "url_link" : url_link,
        "qr_code" : qr_code
    }

@router.put("/{url_id}")
def update_urlLink(url : Annotated[UrlLinksCreate, Body(embed=True)]):
    return {
        "url" : url
    }
