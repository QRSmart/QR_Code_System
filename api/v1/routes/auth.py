from typing import Union, Annotated
from fastapi import APIRouter, Body
from models import storage
from models.users import UsersCreate
from api import firebase_app
from src.auth import create_user, log_user






router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/register")
async def register(user: Annotated[UsersCreate, Body(embed=True)]):
    

    response = await create_user(user=user, firebase=firebase_app)
    print(response)
    #return

    if response["user"] and response["token"]:
        return {
                "success": True,
                "data":response
            }
    #pass

@router.post("/login")
async def signin(user: Annotated[UsersCreate, Body(embed=True)]):
    response = await log_user(user=user)

    print(response)
    if response["user"] and response["token"]:
        return {
                "success": True,
                "data":response
            }
