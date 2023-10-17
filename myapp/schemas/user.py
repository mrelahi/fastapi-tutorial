from pydantic import BaseModel, Field




class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True