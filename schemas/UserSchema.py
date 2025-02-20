from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    bio: Optional[str] = ""

class UserUpdate(BaseModel):
    username : Optional[str] = None
    email : Optional[EmailStr] = None
    password : Optional[str] = None 
    bio : Optional[str] = None
    
class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    bio: str

    class Config:
        from_attributes = True 