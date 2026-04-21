from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependency.dependecy import db_add
from service import user
from schema.users import UserCreate as User_pydantic
from schema.users import Group

router= APIRouter()

@router.post("/add_new")
def add_user(new_user:User_pydantic, db: Session=Depends(db_add)):
    user_dict=new_user.model_dump()
    new=user.add_user(user_dict, db)
    return new

@router.post("/add_group")
def add_group(new_group: Group, db: Session=Depends(db_add)):
    to_dict=new_group.model_dump()
    group_info= user.create_new_group(to_dict, db)
    return group_info

@router.get("/view_groups")
def view_groups(db: Session=Depends(db_add)):
    groups=user.view_groups(db)
    return groups

@router.delete("/delete_group/{id}")
def delete_group(id: int, db: Session=Depends(db_add)):
    return user.delete_group(id, db)

@router.get("/all_group_members/{id}")
def get_all_members(id: int, db:Session=Depends(db_add)):
    members=user.get_group_members(id, db)
    return members
