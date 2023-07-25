from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

"""Pour recevoir le corps dune requete PUT"""
from pydantic import BaseModel
from typing import List
from typing import Set, Tuple
from typing import Optional


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi('hello')

def process_items(items: List[int]):
    for item in items:
        print(item)

print(process_items(['1','2','3']));

app = FastAPI()
def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s


"""Pour recevoir le corps dune requete PUT"""

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


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

qr_codes = [
                {
                    "id": "qr34544",
                    "name": "QR Code 1"
                },

                {
                    "id" : "1r45024",
                    "name" : "QR Code 2"
                },

                {
                    "id" : "qr65964",
                    "name" : "QR Code 3"
                }
            ]

@app.get("/")
def home():
    return {
            "status" : True,
            "message" : "Hello World!"
        }


@app.get("/qr_code/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    for qr_code in qr_codes:
        if qr_code["id"] == item_id:
            return {
                "status" : True,
                "data" : qr_code
            }
    return {
        "status" : True,
        "data" : "Not found"
    }

@app.get("/qr_code")
def read_all_item():
        return {
            "status": True,
            "data": qr_codes
        }

@app.get("/about")
def about():
    return {"About Page"}
