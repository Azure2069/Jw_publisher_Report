from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Date, String

Base=declarative_base()

class Elder(Base):
    __tablename__="Elders"
    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String)
    group=Column(Integer)
    date_of_birth=Column(Date)
    date_of_baptism=Column(Date)

