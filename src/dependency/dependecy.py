from database.database_init import SessionLocal
from fastapi import Request, Depends, HTTPException, Response
from model.users import User as User_table
from model.session import Session as Session_table
from sqlalchemy.orm import Session
from Roles.roles import Roles

def db_add():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()




def get_current_user(request: Request, db: Session=Depends(db_add)):
    token=request.cookies.get("session_token")
    if not token:
        raise HTTPException(status_code=401, detail="not logged in")
    session=db.query(Session_table).filter(Session_table.token==token).first()
    if not session:
        raise HTTPException(status_code=401, detail="session not found")
    user=db.query(User_table).filter(User_table.id==session.user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="user not found")
    return user



def get_admin(current_user=Depends(get_current_user)):
    if current_user.role!=Roles.admin:
        raise HTTPException(status_code=403, detail="Access denied! Account not admin")
    return current_user #here it is an admin


def get_elder(current_user=Depends(get_current_user)):
    if current_user.role!= Roles.elder:
        raise HTTPException(status_code=403, detail="Access Denied! User not Elder")
    return current_user #here it is an elder

def get_group_leader(current_user=Depends(get_elder)):
    if not current_user.is_group_overseer:
        return HTTPException(status_code=403, detail="Access denaid! You are not a group Overseer")
    return current_user #here it is only group overseers

