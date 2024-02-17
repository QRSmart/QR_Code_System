from fastapi import Depends, FastAPI
from api.v1.routes import url_links, business_card

app = FastAPI()

app.include_router(url_links.router)
app.include_router(business_card.router)