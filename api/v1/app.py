"""
Initialisation et configuration de FastAPI
"""
from typing import Union
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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

app.mount("/static_web", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

templatesApp = Jinja2Templates(directory="frontend/templates")



"""
@app.get("/app{full_path:path}")
async def catch_all(request: Request, full_path: str):
    print("full_path: "+full_path)
    return templatesApp.TemplateResponse("index.html", {"request": request})

"""

app.mount("/static", StaticFiles(directory="frontend/build/static", html=True), name="static_app")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request })

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, full_path: str):
    print(full_path)
    #return RedirectResponse(url=request.url.path + "index.html")
    with open("frontend/build/index.html", "r") as file:
        index_html = file.read()
    return HTMLResponse(content=index_html, status_code=200)

# app.mount("/", StaticFiles(directory="frontend/build"), name="static_app")



"""

"""