from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependency.dependecy import db_add
from schema.users import UserCreate
from service import publisher_logic

router=APIRouter()

@router.post("/add_publisher")
def add_publisher(user: UserCreate, db: Session=Depends(db_add)):
    to_dict=user.model_dump()
    return publisher_logic.add_publisher(to_dict, db)

@router.get("/get_publisher/{id}")
def get_publisher_by_id(id: int, db: Session=Depends(db_add)):
    return publisher_logic.get_publisher_by_id(id, db)

@router.get("/get_all")
def get_all_publishers(db: Session=Depends(db_add)):
    return publisher_logic.get_all(db)

@router.delete("/delete_publisher")
def delete_publisher(id: int, db: Session=Depends(db_add)):
    deleted=publisher_logic.delete(id, db)
    return "success"

@router.put("/update_publisher")
def update_publisher(id: int, user: UserCreate, db: Session=Depends(db_add)):
    user_dict=user.model_dump()
    updated=publisher_logic.update(id, user_dict, db)
    return updated