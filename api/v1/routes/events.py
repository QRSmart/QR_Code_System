from typing import Union, Annotated
from fastapi import APIRouter, Body
from models import storage
from models.events import Events, EventsCreate, EventsScheme
router = APIRouter(prefix="/events",tags=["Events"])

"""
Events QR_codes Routes
"""
@router.get("/{event_id}")
def read_eventsLink(event_id: int, q: Union[str, None] = None):
    """
    Get a events by its id
    :param event_id: events object id
    """
    print(event_id)
    events = storage.get("events", event_id)
    if events is not None:         
        return {
            "status" : True,
            "data" : events
        }

@router.get("/{user_id}")
def get_events():
    """
        Get all eventss links of a user
    """
    return None

@router.post("")
def create_eventsLink(events : Annotated[EventsCreate, Body(embed=True)]):
    """
    Cree un lien qrcode
    """
    
    events_link = Events(title=events.title, location=events.location, start_date=events.start, end_date=events.end)
    
    qr_code = events_link.generate(1, events)
    
    events_link.save()
    
    

    return {
        "events_link" : events_link,
        "qr_code" : qr_code
    }

@router.put("/{event_id}")
def update_eventsLink(events : Annotated[EventsCreate, Body(embed=True)]):
    return {
        "events" : events
    }
