"""
Initialisation et configuration de FastAPI
"""

from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api_v1 import app

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

@app.get("/")
async def root():
    return {
        "message" : "Hello QRSmart!"
    }