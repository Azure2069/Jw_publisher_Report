from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.orm import relationship
from database.database_init import Base


class Elder(Base):
    __tablename__="Elders"
    elder_id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    group=Column(Integer)
    date_of_birth=Column(Date)
    date_of_baptism=Column(Date)
    managed_group=relationship("Groups", back_populates="overseer")

