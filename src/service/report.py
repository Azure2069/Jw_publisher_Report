from sqlalchemy.orm import Session
from repository import report
from repository import report

def add_report(report1: dict, name: str, db:Session):
    new_report=report.add_new_report(report1, name, db)
    return new_report