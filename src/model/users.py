from sqlalchemy.orm import Session, relationship
from sqlalchemy import Integer, Float, String, ForeignKey, Column, Boolean, Date, Enum
from datetime import date
from Roles.roles import Roles
from model.elder import Elder
from database.database_init import Base


class All_Users(Base):
    __tablename__="publishers"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    group=Column(Integer)
    is_baptized=Column(Boolean)
    date_of_baptism=Column(Date)
    date_of_birth=Column(Date)
    gender=Column(String)
    role= Column(Enum(Roles))


class Groups(Base):
    __tablename__="groups"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(Integer)
    overseer_id=Column(Integer, ForeignKey("Elders.elder_id"))
    overseer=relationship("Elder", back_populates="managed_group")