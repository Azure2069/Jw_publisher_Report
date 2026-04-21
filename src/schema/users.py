from pydantic import BaseModel
from datetime import date
from Roles.roles import Roles
from typing import Optional

class UserCreate(BaseModel):
    name: str
    date_of_birth: date
    group_id: int
    is_baptized: bool
    date_of_baptism: Optional[date] = None
    gender: str
    role: Roles
    is_group_overseer: bool =False

class UserDb(BaseModel):
    name: str
    date_of_birth: date
    group: int
    is_baptized: bool
    date_of_baptism: date
    Gender: str
    role: Roles
    date_created: date


class UserResponse(BaseModel):
    id: int
    name: str
    group: int
    role: Roles
    is_baptized: bool


class publisher_report(BaseModel):
    month: date
    participated: bool
    bible_studies: int


class auxiliary_pioneer(publisher_report):
    hours: int

class regular_pioneer_report(publisher_report):
    hours: int
    placement: int


class Group(BaseModel):
    name: str


