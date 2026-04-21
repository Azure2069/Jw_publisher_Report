from sqlalchemy.orm import Session, relationship
from sqlalchemy import Integer, Float, String, ForeignKey, Column, Boolean, Date, Enum
from datetime import date
from Roles.roles import Roles
#from model.elder import Elder
from database.database_init import Base
from model.report import Report


class User(Base):
    __tablename__="publishers"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    is_baptized=Column(Boolean)
    date_of_baptism=Column(Date)
    date_of_birth=Column(Date)
    gender=Column(String)
    role= Column(Enum(Roles))
    is_group_overseer=Column(Boolean)
    group_id=Column(Integer, ForeignKey("groups.id"))
    group=relationship("Group", back_populates="members", foreign_keys=[group_id])
    led_group=relationship("Group", back_populates="overseer", foreign_keys="Group.overseer_id")
    monthly_report=relationship("Report", back_populates="publisher", foreign_keys="Report.user_id")




class Group(Base):
    __tablename__="groups"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    overseer_id=Column(Integer, ForeignKey("publishers.id"), nullable=True)
    overseer=relationship("User", back_populates="led_group", foreign_keys=[overseer_id])
    members=relationship("User", back_populates="group", foreign_keys="User.group_id")


def age():
    pass