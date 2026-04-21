from sqlalchemy.orm import relationship

from database.database_init import Base
from Roles import roles
from sqlalchemy import ForeignKey, Integer, String, Date, Column, Boolean


class Report(Base):
    __tablename__="reports"
    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    month_name=Column(Integer)
    participated=Column(Boolean)
    hours=Column(Integer)
    bible_studies=Column(Integer)
    placement=Column(Integer)
    user_id=Column(Integer, ForeignKey("publishers.id"))
    publisher=relationship("User", back_populates="monthly_report", foreign_keys=[user_id])