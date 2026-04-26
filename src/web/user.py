from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependency.dependecy import db_add, get_group_leader, get_current_user, get_admin, get_elder
from service import user, auth
from schema.users import UserCreate as User_pydantic
from schema.users import Group


router= APIRouter()

@router.post("/add_new")
def add_user(new_user:User_pydantic, db: Session=Depends(db_add), _=Depends(get_admin)):
    user_dict=new_user.model_dump()
    password=user_dict.pop("password")
    new=user.add_user(user_dict, password, db)
    return new

@router.get("/get_your_info")
def get_your_info(db: Session=Depends(db_add), you=Depends(get_current_user)):
    info=user.get_one_by_id(you.id, db)
    return info

@router.post("/add_group")
def add_group(new_group: Group, db: Session=Depends(db_add), _=Depends(get_admin)):
    to_dict=new_group.model_dump()
    group_info= user.create_new_group(to_dict, db)
    return group_info

@router.delete("/delete_user")
def delete_user(id: int, db: Session=Depends(db_add), _=Depends(get_admin)):
    deleted=user.delete(id, db)
    return deleted

@router.get("/view_groups")
def view_groups(db: Session=Depends(db_add),  _=Depends(get_elder)):
    groups=user.view_groups(db)
    return groups

@router.delete("/delete_group/{id}")
def delete_group(id: int, db: Session=Depends(db_add), _=Depends(get_admin)):
    return user.delete_group(id, db)

@router.get("/all_group_members/{id}")
def get_all_members(id: int, db:Session=Depends(db_add), _=Depends(get_elder)):
    members=user.get_group_members(id, db)
    return members
