from sqlalchemy.orm import Session, relationship
from sqlalchemy import Integer, Float, String, ForeignKey, Column, Boolean, Date, Enum
from datetime import date
from Roles.roles import Roles
from model.elder import Elder
from database.database_init import Base


class All_Users(Base):
    __tablename__="publishers"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    is_baptized=Column(Boolean)
    date_of_baptism=Column(Date)
    date_of_birth=Column(Date)
    gender=Column(String)
    role= Column(Enum(Roles))
    group_id=Column(Integer, ForeignKey("groups.id"))
    group=relationship("Groups", back_populates="user")
    elder_profile=relationship("Elder", back_populates="user_profile")



class Groups(Base):
    __tablename__="groups"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(Integer)
    overseer_id=Column(Integer, ForeignKey("Elders.elder_id"))
    overseer=relationship("Elder", back_populates="managed_group")
    user=relationship("All_users", back_populates="group")