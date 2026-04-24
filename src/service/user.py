from sqlalchemy.orm import Session
from repository import user


def add_user(n_user: dict, password, db: Session):
    new_user = user.create_user(n_user, password, db)
    if not new_user:
        return "user creation unsuccessful"

    return new_user


def get_by_id(id: int, db: Session):
    new_user = user.get_one_by_id(id, db)
    if not new_user:
        return "user not found"
    return new_user


def get_all(db: Session):
    all_users = user.get_all_users(db)
    if not all_users:
        return "no user found"
    return all_users


def delete(id: int, db: Session):
    user.delete_user_by_id(id, db)
    return "successfully deleted user"


def create_new_group(group: dict, db: Session):
    new_group = user.create_group(group, db)
    return new_group


def view_groups(db: Session):
    groups = user.view_groups(db)
    return groups


def delete_group(id: int, db: Session):
    return user.delete_group(id, db)

def get_group_members(id:int, db: Session):
    return user.get_group_members(id, db)
