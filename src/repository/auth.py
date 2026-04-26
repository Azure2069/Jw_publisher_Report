from Roles.roles import Roles
import bcrypt
from sqlalchemy.orm import Session
from fastapi import HTTPException, Request, Depends
from model.session import Session as Session_table
from model.users import User as User_table
import secrets
from dependency.dependecy import db_add


def hash_password(password: str)->str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_passpord(password: str, hashed_password: str):
    verified_password=bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
    return verified_password

def generate_session_token():
    token=secrets.token_hex(32)
    return token

def login(username: str, password: str, db: Session):
    hashed_password=hash_password(password)
    user=db.query(User_table).filter(User_table.username==username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    verified_password=verify_passpord(password, user.hashed_password)
    if not verified_password:
        raise HTTPException(status_code=401, detail="username or password incorrect")
    token=generate_session_token()
    session=Session_table(token=token, user_id=user.id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return token



def delete_session(token: str, db: Session):
    session=db.query(Session_table).filter(Session_table.token==token).first()
    if not session:
        raise HTTPException(status_code=401, detail="session not found")
    db.delete(session)
    db.commit()


