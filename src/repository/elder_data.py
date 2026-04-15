from sqlalchemy.orm import Session
from model.elder import Elder as Elder_table



def add_elder(db: Session, elder: dict):
    new_elder=Elder_table(**elder)
    db.add(new_elder)
    db.commit()
    db.refresh(new_elder)
    return new_elder

def delete_elder(id: int, db: Session):
    elder=db.query(Elder_table).filter(id==Elder_table.elder_id).first()
    if elder:
        db.delete(elder)
        db.commit()
        return "success"
    return "elder not found!"


def view_all(db: Session):
    all_elders=db.query(Elder_table).all()
    return all_elders

def get_by_id(id: int, db: Session):
    elder1=db.query(Elder_table).filter(id==Elder_table.id).first()
    return elder1

def update_elder(id: int, elder: dict, db: Session):
    new_elder=db.query(Elder_table).filter(id==Elder_table.elder_id).first()
    if not new_elder:
        return "elder not found"
    new_elder.name=elder.get("name")
    new_elder.group = elder.get("group")
    new_elder.date_of_birth = elder.get("date_of_birth")
    new_elder.date_of_baptism = elder.get("date_of_baptism")
    db.commit()
    return new_elder

