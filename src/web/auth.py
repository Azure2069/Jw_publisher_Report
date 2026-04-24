from fastapi import APIRouter, Response, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from dependency.dependecy import db_add


router=APIRouter()
from service import auth

@router.post("/login")
def login(username: str, password: str, response:Response, db: Session=Depends(db_add)):
    token1=auth.login(username, password, db)
    response.set_cookie(key="session_token", value=token1, httponly=True)
    return {"message": "log in successful"}

@router.post("/logout")
def logout(request: Request, response: Response, db:Session=Depends(db_add)):
    auth.logout(request, db)
    response.delete_cookie(key="session_token")
    return{"message": "logout success"}


