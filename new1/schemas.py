from pydantic import BaseModel

class UserCreate(BaseModel):
    name : str
    age: int
    skills: list[str]

class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode= True