from fastapi import FastAPI
from database import engine,Base
from routes import users

Base.metadata.create_all(bind= engine)


app = FastAPI()


app.include_router(users.router, prefix= "/users", tags=["Users"])


























# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# @app.get("/")
# def home():
#     return{"messege":"Backend is alive"}

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return{"user_id": user_id}


# @app.get("/search")
# def search(q: str, limit: int = 10):
#     return{"query": q, "limit": limit}


# class User(BaseModel):
#     name: str
#     age: int
#     skills: list[str]

# @app.post("/users")
# def create_user(user: User):
#     return {"user": user}

# from passlib.hash import bcrypt

# hashed = bcrypt.hash("mypass")
# bcrypt.verify("mypass",hashed)