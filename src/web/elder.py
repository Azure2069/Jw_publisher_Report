from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model.elder import Elder
from schema.elder import Elder
from service import elder_logic
from dependency.dependecy import db_add
router=APIRouter()


@router.get("/")
def testing():
    return{
        "message": "lets get started!"
    }
@router.post("/add_elder")
def add_elder(new_elder: Elder, db: Session=Depends(db_add)):
    elder_dict=new_elder.model_dump()
    elder=elder_logic.add_elder(db, elder_dict)
    if not elder:
        return{"error": "something occured"}
    return {
        "message": f"{elder.name} successfully added"
    }

@router.delete("/delete_elder/{id}")
def delete_elder(id: int, db: Session=Depends(db_add)):
    elder_logic.delete_elder(id, db)


@router.get("/all_elders")
def view_all(db: Session=Depends(db_add)):
    all_elders=elder_logic.view_all(db)
    if not all_elders:
        return "no elder found"
    return all_elders

@router.get("/get_by_id/{id}")
def get_by_id(id: int, db: Session=Depends(db_add)):
    elder=elder_logic.get_by_id(id, db)
    if not elder:
        return "elder does not exist"
    return elder

#a problem to solve. come back later

@router.put("/update")
def update_elder(id: int, elder: Elder, db: Session=Depends(db_add)):
    elder_dict=elder.model_dump()
    elder1=elder_logic.update_elder(id, elder_dict, db)
    if not elder1:
        return "elder not found"

    return f"elder  successfully updated {elder.name}"