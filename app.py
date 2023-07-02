from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

qr_codes = [
                {
                    "id" : "qr34544",
                    "name" : "QR Code 1"
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
            "status" : True,
            "data" : qr_codes
        }

@app.get("/about")
def about():
    return {"About Page"}
