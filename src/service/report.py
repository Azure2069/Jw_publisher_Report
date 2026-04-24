from sqlalchemy.orm import Session
from repository import report
from repository import report

def add_report(report1: dict, id: int, db:Session):
    publisher=report.get_publisher(id, db)
    validated_report=report.validate_report(report1, publisher)
    new_report=report.add_report(validated_report, db)
    return new_report


def view_report_by_user_id(id: int, db: Session):
    reports=report.view_report_by_user_id(id, db)
