# from pydantic import BaseModel
from database import Base
from sqlalchemy import String, Integer, Column


# class User(BaseModel):
#     name: str
#     age: int
#     skills: list[str]

#     class Config:
#         orm_mode = True

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key= True, index = True)
    name = Column(String, index= True)
    age = Column(Integer)
    skills = Column(String)