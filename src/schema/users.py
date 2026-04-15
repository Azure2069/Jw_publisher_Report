from pydantic import BaseModel
from datetime import date
from Roles.roles import Roles

class UserCreate(BaseModel):
    name: str
    date_of_birth: date
    group: int
    is_baptized: bool
    date_of_baptism: date
    Gender: str
    role: Roles


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
    class UserResponse(BaseModel):
        id: int
        name: str
        group: int
        role: Roles
        is_baptized: bool