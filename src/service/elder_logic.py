"""from repository import elder_data
from sqlalchemy.orm import Session

def add_elder(db: Session, elder: dict):
    return elder_data.add_elder(db, elder)

def delete_elder(id: int, db: Session):
    elder_data.delete_elder(id, db)


def view_all(db: Session):
    return elder_data.view_all(db)


def get_by_id(id: int, db: Session):
    return elder_data.get_by_id(id, db)


def update_elder(id: int, elder: dict, db: Session):
    updated_elder=elder_data.update_elder(id, elder, db)
    if not updated_elder:
        return None
    return updated_elder
"""