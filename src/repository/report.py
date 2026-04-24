from sqlalchemy.orm import Session
from model.report import Report as report_table
from model.users import User as user_table
from Roles.roles import Roles

from fastapi import HTTPException

def get_publisher(id: int, db: Session):
    publisher = db.query(user_table).filter(user_table.id == id).first()
    if not publisher:
        raise HTTPException(status_code=402, detail="publisher cannot be found")
    return publisher


def validate_report(report: dict, publisher):
    report["id"] = publisher.id
    report["user_id"] = publisher.id
    if publisher.role == Roles.elder or publisher.role == Roles.publisher:
        report["hours"] = None
        report["placement"] = None
    if publisher.role == Roles.auxiliary_pioneer:
        report["placement"] = None
    if report.get("participated") == False:
        report["bible_studies"] = None
        return report



def add_report(report: dict, db: Session):
    new_report=report_table(**report)
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report

"""def add_new_report(report: dict, id: int, db: Session):
    publisher=db.query(user_table).filter(user_table.id==id).first()
    if not publisher:
        return "publisher does not exist"
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
"""

def view_report_by_user_id(id: int, db: Session):
    repor=db.query(report_table).filter(report_table.user_id==id).all()
    if not repor:
        raise HTTPException(status_code=404, detail="user not found")
    return repor