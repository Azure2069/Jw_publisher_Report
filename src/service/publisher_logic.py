"""from sqlalchemy.orm import Session


from repository import publisher_data

def add_publisher(user: dict, db: Session):
    new_publisher=publisher_data.add_new_publisher(user, db)
    return new_publisher

def get_publisher_by_id(id: int, db: Session):
    publisher=publisher_data.get_publisher_by_id(id, db)
    if not publisher:
        return "publisher not found"
    return publisher

def get_all(db: Session):
    all_publishers=publisher_data.get_all(db)
    if all_publishers:
        return all_publishers
    return "publisher Empty"

def delete(id, db: Session):
    publisher_data.delete_publisher(id, db)

def update(id, user: dict, db: Session):
    updated_publisher=publisher_data.update(id, user, db)
    if not updated_publisher:
        return "update unsuccessful"
    return updated_publisher"""