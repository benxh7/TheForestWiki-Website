from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    date_joined: datetime
    date_joined_ts: int

class CommentaryIn(BaseModel):
    content: str
    parent: Optional[int] = None

class CommentaryOut(BaseModel):
    id: int
    content: str
    usuario: str
    created: datetime
    updated: datetime
    parent: Optional[int]
    replies: List["CommentaryOut"] = []

CommentaryOut.update_forward_refs()