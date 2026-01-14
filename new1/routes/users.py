from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import UserCreate, UserResponse




router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/",response_model=UserResponse)
def create_user(user: UserCreate, db:Session= Depends(get_db)):
    db_user = User(
        name = user.name,
        age=user.age,
        skills = ",".join(user.skills)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    result = []
    for u in users:
        result.append({
            "id": u.id,
            "name": u.name,
            "age": u.age,
            "skills": u.skills.split(",") if u.skills else []
        })
    return result
















# from fastapi import APIRouter
# from models import User


# router = APIRouter()
# users = []
# next_id = 1

# @router.post("/")
# def add_user(user: User):
#     global next_id
#     user_data = user.dict()
#     user_data["id"] = next_id
#     next_id += 1
#     users.append(user_data)
#     return user_data

# @router.get("/{user_id}")
# def get_user(user_id: int):
#     for user in users:
#         if(user["id"] == user_id):
#             return user["name"]
#     return {"messege": "User not found"}, 404

# @router.delete("/{user_id}")
# def delete_user(user_id : int):
#     for user in users:
#         if(user["id"] == user_id):
#             users.remove(user)
#             return user
#     return {"messege": "User not found"}, 404


# @router.get("/")
# def get_users():
#     return [useer.dict() for useer in users] 

# @router.post("/")
# def add_user(user: User):
#     users.append(user.name)
#     return user
 

