from pydantic import BaseModel, Field


class UserBase(BaseModel):
    first_name: str  
    last_name: str 
    gender: str 
    email: str 

class UserCreate(UserBase):
    username: str
    password: str 

class UserUpdate(UserBase):
    username: str
  
class User(UserBase):
    id: int
    is_active: bool


