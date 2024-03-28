from typing import Optional
from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    first_name: str
    last_name: str
    password: str
