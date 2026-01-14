from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime





class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index=True)
    age = Column(Integer)
    skills = Column(String)
    created_at = Column(DateTime, default= datetime.utcnow)
    password = Column(String)

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    price = Column(Integer)
    created_at = Column(DateTime, default= datetime.utcnow)