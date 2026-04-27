from sqlalchemy.orm import Session
from model.users import User as User_table
from model.users import Group as Group_table
from fastapi import HTTPException
from Roles.roles import Roles
from repository.auth import hash_password


#def add_admin(user_info: dict, db: Session):
    #admin = User_table(**user_info)
    #db.add(admin)
   # db.commit()
  #  db.refresh(admin)
 #   return admin


def create_user(user: dict, password: str, db: Session):

    group=db.query(Group_table).filter(Group_table.id==user.get("group_id")).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    if (user.get("role")== Roles.elder or user.get("role")==Roles.pioneer_elder) and not user.get("is_baptized"):
        raise HTTPException(status_code=404, detail="elders are always baptized")
    if user.get("role")==Roles.regular_pioneer and user.get("is_baptized")==False:
        raise HTTPException(status_code=404, detail="pioneers are always baptized")
    if user.get("role")==Roles.auxiliary_pioneer and user.get("is_baptized")==False:
        raise HTTPException(status_code=404, detail="auxiliary pioneer must be baptized")
    forbidden_roles=[Roles.admin, Roles.elder, Roles.pioneer_elder]
    if user.get("role") not in forbidden_roles and user.get("is_group_overseer"):
        raise HTTPException(status_code=403, detail="Only elders qualify to be Group Overseers")
    user["hashed_password"]=hash_password(password)
    new_user = User_table(**user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    if new_user.role=="elder" and new_user.is_group_overseer:
        group.overseer_id=new_user.id
        db.commit()
    return new_user

def get_all_users(db: Session):
    all_users=db.query(User_table).all()
    return all_users



def get_one_by_id(id: int, db: Session):
    user=db.query(User_table).filter(User_table.id==id).first()
    return user

def delete_user_by_id(id: int, db: Session):
    user=db.query(User_table).filter(User_table.id==id)
    db.delete(user)

def update_user(id: int, updates: dict, db: Session):
    user=db.query(User_table).filter(User_table.id==id).first()
    if not user:
        raise HTTPException(status_code=401, detail="user not found")
    for key, value in updates.items():
        if value != None:
            setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user
#left error here. check how to do proper update function



def create_group(group: dict, db: Session):
    new_group=Group_table(**group)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group

def view_groups(db: Session):
    groups=db.query(Group_table).all()
    return groups

def delete_group(id: int, db: Session):
    group=db.query(Group_table).filter(Group_table.id==id).first()
    if not group:
        return "Group does not exist"
    db.delete(group)
    db.commit()
    return "group successfully created"

def get_group_members(id: int, db: Session):
    group=db.query(Group_table).filter(Group_table.id==id).first()
    if not group:
        return "Group does not exist"
    if not group.members:
        return "there are no members"
    return group.members