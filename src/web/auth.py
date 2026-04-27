from fastapi import APIRouter, Response, Request
from fastapi import Depends
from sqlalchemy.orm import Session
from dependency.dependecy import db_add
from dependency.dependecy import get_admin, get_current_user

router=APIRouter()
from service import auth

@router.post("/login")
def login(username: str, password: str, response:Response, db: Session=Depends(db_add)):
    token1=auth.login(username, password, db)
    response.set_cookie(key="session_token", value=token1, httponly=True)
    return {"message": "log in successful"}

@router.post("/logout")
def logout(request: Request, response: Response, db:Session=Depends(db_add), _=Depends(get_current_user)):
    auth.logout(request, db)
    response.delete_cookie(key="session_token")
    return{"message": "logout success"}


@router.patch("/change_password")
def change_password(old_password, new_password, db: Session=Depends(db_add), current_user=Depends(get_current_user)):
    return auth.change_password(current_user.id, old_password, new_password, db)