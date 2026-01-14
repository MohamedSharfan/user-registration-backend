from pydantic import Field, conint, BaseModel
from sqlalchemy import DateTime
from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from models import User  # SQLAlchemy ORM model
from database import get_db

router = APIRouter()

@router.get("/users/{id}")
def get_user(id : int):
    for user in users:
        if(user["id"] == id):
            return user
    return {"messege":"user not found"}

@router.delete("users/{id}")
def delete_user(id : int, db: Session=Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
    raise HTTPException(status_code=404,detail="User not found")



class UserCreate(BaseModel):
    name : str = Field(
        min_length=3
    )
    age: conint(ge=16)
    skills: list[str] = Field(
        ..., min_items = 1
    )



class CreateUser(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    name: str
    created_at : DateTime


    class Config:
        orm_mode = True


class User(BaseModel):
    created_at : DateTime
