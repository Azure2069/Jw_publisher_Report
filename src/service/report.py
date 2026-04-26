from fastapi.params import Depends
from sqlalchemy.orm import Session
from repository import report
from repository import report
from Roles.roles import Roles


def get_publisher(username: str, db: Session):
    return report.get_publisher(username, db)

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



def add_report(validated_report, db:Session):
    new_report=report.add_report(validated_report, db)
    return new_report




#def add_report(report1: dict, db:Session, publisher=Depends(report.get_publisher), validated_report=Depends(report.validate_report())):
    #validated_report=report.validate_report(report1, publisher)
 #   new_report=report.add_report(validated_report, db)
  #  return

def get_all_reports(db: Session):
    return report.view_all_reports(db)

def view_reports_by_group(group_id, db: Session):
    return report.view_report_by_group(group_id, db)

def get_report_by_id(user_id: int, db: Session):
    return report.get_reports_by_id(user_id, db)