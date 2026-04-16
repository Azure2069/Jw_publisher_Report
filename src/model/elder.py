from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database_init import Base


class Elder(Base):
    __tablename__="Elders"
    elder_id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id=Column(ForeignKey("publishers.id"))
    group_id=Column(ForeignKey("groups.id"))
    managed_group=relationship("Groups", back_populates="overseer")
    user_profile=relationship("All_users", back_populates="elder_profile")


