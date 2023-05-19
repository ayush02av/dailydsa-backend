from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TempToken(BaseModel):
    email: str
    given_name: str
    family_name: str
    nickname: str
    email: str
    sub: str
    picture: str

class AuthToken(BaseModel):
    id: str
    username: str
    email: str

class EntryRequest(BaseModel):
    token: str

class EntryResponse(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    picture: str
    last_submission: Optional[datetime]
    is_admin: bool
    token: Optional[str]