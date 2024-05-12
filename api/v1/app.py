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
from api.config import get_settings, get_firebase_app
import pathlib
#rom dotenv import load_dotenv

#load_dotenv()

settings = get_settings()
origins = [ settings.frontend_url , "http://localhost" ]




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


app.mount("/static", StaticFiles(directory="frontend/build/static", html=True), name="static_app")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request })
@app.get("/about", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("about.html", context={"request": request })

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def catch_all(request: Request, full_path: str):
    print(full_path)
    #return RedirectResponse(url=request.url.path + "index.html")
    with open("frontend/build/index.html", "r") as file:
        index_html = file.read()
    return HTMLResponse(content=index_html, status_code=200)
