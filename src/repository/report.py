from sqlalchemy.orm import Session
from model.report import Report as report_table
from model.users import User as user_table
from Roles.roles import Roles

from fastapi import HTTPException

def add_new_report(report: dict, name: str, db: Session):
    publisher=db.query(user_table).filter(user_table.name==name).first()
    report["id"]=publisher.id
    report["user_id"]=publisher.id
    if publisher.role== Roles.elder or publisher.role==Roles.publisher:
        report["hours"]=None
        report["placement"]=None
    if publisher.role==Roles.auxiliary_pioneer:
        report["placement"]=None
    if report.get("participated")==False:
        report["bible_studies"]=None
    new_report=report_table(**report)
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report


