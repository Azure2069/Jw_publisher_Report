from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from service import report
from schema.report import Report
from dependency.dependecy import db_add

router=APIRouter()

@router.post("/add_report")
def add_report(report2: Report, name: str, db: Session=Depends(db_add)):
    to_dict=report2.model_dump()
    return report.add_report(to_dict, name, db)