from fastapi.params import Depends
from sqlalchemy.orm import Session
from model.report import Report as Report_table
from model.users import User as user_table
from Roles.roles import Roles

from fastapi import HTTPException

def get_publisher(username: str, db: Session):
    publisher = db.query(user_table).filter(user_table.username == username).first()
    if not publisher:
        raise HTTPException(status_code=402, detail="publisher cannot be found")
    return publisher

def get_reports_by_id(user_id: int, db: Session):
    reports=db.query(Report_table).filter(Report_table.user_id==user_id).all()
    return reports



def add_report(report: dict, db: Session):
    new_report=Report_table(**report)
    db.add(new_report)
    db.commit()
    db.refresh(new_report)
    return new_report


def view_all_reports(db:Session):
    reports=db.query(Report_table).all()
    if not reports:
        raise HTTPException(status_code=404, detail="No reports found")
    return reports

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

def view_report_by_group(group_id: int, db: Session):
    repor=db.query(Report_table).filter(Report_table.group_id==group_id).all()
    if not repor:
        raise HTTPException(status_code=404, detail="group report not found")
    return repor