from pydantic import BaseModel
from datetime import date

class Elder(BaseModel):
    id: int
    name: str
    group: int
    date_of_birth: date
    date_of_baptism: date