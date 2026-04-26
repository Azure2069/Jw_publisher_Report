from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from service import report
from schema.report import Report
from dependency.dependecy import db_add, get_current_user, get_admin, get_elder, get_group_leader
from service import auth

router=APIRouter()

@router.post("/add_report")
def add_report(report2: Report, username: str, db: Session=Depends(db_add), user=Depends(get_current_user)):
    to_dict=report2.model_dump()
    publisher=report.get_publisher(username, db)
    validated_report=report.validate_report(to_dict, publisher)
    new_report=report.add_report(validated_report, db)
    return new_report



@router.get("/all_user_reports")
def all_user_report(db: Session=Depends(db_add), _=Depends(get_elder)):
    reports=report.get_all_reports(db)
    return reports

@router.get("/all_report_by_group")
def all_report_by_group(db: Session=Depends(db_add), elder=Depends(get_group_leader)):
    group_name=elder.group_id
    reports=report.view_reports_by_group(group_name, db)
    return reports

@router.get("/get_reports_by_user")
def get_reports_by_user(db: Session=Depends(db_add), user=Depends(get_current_user)):
    reports=report.get_report_by_id(user.id, db)
    return reports