from pydantic import BaseModel, Field
from datetime import datetime


class UserCreate(BaseModel):
    name : str = Field(min_length = 3)
    age : int = Field(ge=16) 
    skills: list[str] = Field(min_items = 1)
    password: str


class UserResponse(BaseModel):
    id: int
    name : str
    age: int
    skills : list[str]
    created_at: datetime

    class Config:
        from_attributes = True


class Item(BaseModel):
    title: str
    description: str | None = None


class ProductCreate(BaseModel):
    name: str
    price: int

class ProductResponse(BaseModel):
    id: int
    name: str
    price: int
    created_at: datetime
    
    class Config:
        from_attributes = True