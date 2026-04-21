from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
class Report(BaseModel):
    month_name: int=Field(..., ge=1, le=12)
    participated: bool
    hours: int| None=None
    bible_studies: int|None=None
    placement: int|None=None