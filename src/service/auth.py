from http.client import HTTPException

from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi import Request, Response, HTTPException
from dependency import dependecy

from dependency.dependecy import db_add
from repository import auth

def login(username: str, password: str, db: Session):
    return auth.login(username, password, db)


def get_current_user(request: Request, db: Session=Depends(db_add)):
    return dependecy.get_current_user(request, db)

def logout(request: Request, db: Session=Depends(db_add)):
    token=request.cookies.get("session_token")
    if not token:
        raise HTTPException(status_code=401, detail="not logged in")
    auth.delete_session(token, db)
    return {"message": "logout successfully"}


"""
def get_elder(current_user=Depends(get_current_user)):
    return current_user

def get_admin(current_user=Depends(get_current_user)):
    return current_user
"""


def change_password(id: int, old_password: str, new_password: str, db: Session):
    return auth.change_password(id, old_password, new_password, db)
