from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model.elder import Elder
from schema.elder import Elder
from model.elder import Elder as elder_table
from dependency.dependecy import db_add
router=APIRouter()


@router.get("/")
def testing():
    return{
        "message": "lets get started!"
    }
@router.post("/add_elder")
def add_elder(new_elder: Elder, db: Session=Depends(db_add)):
    db.add(elder_table(**new_elder.model_dump()))
    db.commit()
    return {
        "message": f"{new_elder.name} successfully added"
    }

@router.delete("/delete_elder/{id}")
def delete_elder(id: int, db: Session=Depends(db_add)):
    elder=db.query(elder_table).filter(id==elder_table.id).first()
    if not elder:
        return "elder id does not exist"
    db.delete(elder)
    db.commit()
    return {"message": "Elder successfully deleted"}

@router.get("/all_elders")
def view_all(db: Session=Depends(db_add)):
    all_elders=db.query(elder_table).all()
    if not all_elders:
        return "no elder found"
    return all_elders

@router.get("/get_by_id/{id}")
def get_by_id(id: int, db: Session=Depends(db_add)):
    elder=db.query(elder_table).filter(id==elder_table.id).first()
    if not elder:
        return "elder does not exist"
    return elder


@router.put("/update")
def update_elder(id: int, elder: Elder, db: Session=Depends(db_add)):
    elder1=db.query(elder_table).filter(id==elder_table.id).first()
    if not elder1:
        return "elder not found"

    elder1.name=elder.name
    elder1.group=elder.group
    elder1.date_of_birth=elder.date_of_birth
    elder1.date_of_baptism=elder.date_of_baptism
    db.commit()
    return f"{elder1.name}  successfully updated {elder.name}"