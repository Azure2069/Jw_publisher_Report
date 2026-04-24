from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from service import report
from schema.report import Report
from dependency.dependecy import db_add
from service import auth

router=APIRouter()

@router.post("/add_report")
def add_report(report2: Report, id: int, db: Session=Depends(db_add), _=Depends(auth.get_current_user)):
    to_dict=report2.model_dump()
    return report.add_report(to_dict, id, db)

@router.get("/all_user_report")
def all_user_report(id: int, db: Session=Depends(db_add), _=Depends(auth.get_current_user)):
    reports=report.view_report_by_user_id(id, db)