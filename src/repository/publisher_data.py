from fastapi import Depends
from sqlalchemy.orm import Session


from model.users import All_Users as User_table


def add_new_publisher(user: dict, db: Session):
    check=db.query(User_table).filter(User_table.name.ilike(user.get("name")),
                                      User_table.date_of_birth == user.get("date_of_birth")).first()
    if not check:
        new_publisher=User_table(**user)
        db.add(new_publisher)
        db.commit()
        db.refresh(new_publisher)
        return new_publisher
    return {
        "error": "User Exist already"
    }
def get_publisher_by_id(id: int, db: Session):
    publisher=db.query(User_table).filter(User_table.id==id).first()
    return publisher

def get_all(db:Session):
    all_publishers=db.query(User_table).all()
    return all_publishers

def delete_publisher(id: int, db: Session):
    publisher=db.query(User_table).filter(User_table.id==id).first()
    db.delete(publisher)
    db.commit()
    return "publisher deleted"

def update(id: int, user: dict, db: Session):
    publisher=db.query(User_table).filter(User_table.id==id).first()
    if not publisher:
        return "publisher does not exist"
    publisher.name = user.get("name")
    publisher.date_of_birth = user.get("date_of_birth")
    publisher.group = user.get("group")
    publisher.date_of_baptism = user.get("date_of_baptism")
    publisher.gender = user.get("gender")
    publisher.role = user.get("role")
    publisher.is_baptized = user.get("is_baptized")
    db.commit()
    db.refresh(publisher)
    return publisher
