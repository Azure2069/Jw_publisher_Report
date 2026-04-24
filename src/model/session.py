from fastapi.datastructures import Default
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from database.database_init import Base
from datetime import datetime

class Session(Base):
    __tablename__="sessions"
    id=Column(Integer, primary_key=True, autoincrement=True)
    user_id=Column(Integer, ForeignKey("publishers.id"))
    token=Column(String, unique=True)
    created_at=Column(DateTime, default=datetime.utcnow)