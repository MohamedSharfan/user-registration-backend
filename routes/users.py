from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse, Item
from database import SessionLocal
from models import User
from dependencies.auth import get_current_user
from core.security import hash_password, verify_password, create_access_token
from datetime import timedelta
from typing import Optional

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()
auth_router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Hash the password before storing
    hashed_password = hash_password(user.password)
    
    db_user = User(
        name = user.name,
        age = user.age,
        skills = ",".join(user.skills),
        password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    db_user.skills = db_user.skills.split(",")
    return db_user


@router.get("/", response_model = list[UserResponse])
def get_user(db: Session = Depends(get_db)):
    users = db.query(User).all()
    for u in users:
        u.skills = u.skills.split(",")
    return users

@router.get("/me")
def read_current_user(current_user = Depends(get_current_user)):
    return current_user

@router.get("/{stu_id}", response_model = UserResponse)
def get_user(stu_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == stu_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail= "User not found")
    
    user.skills = user.skills.split(",")
    return user


@auth_router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Find user by name (username field in form)
    user = db.query(User).filter(User.name == form_data.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Verify password
    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Create access token
    access_token = create_access_token(
        data={"sub": user.name, "user_id": user.id},
        expires_delta=timedelta(hours=24)
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.delete("/{stu_id}")
def delete_user(stu_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    user = db.query(User).filter(User.id == stu_id).first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    db.delete(user)
    db.commit()
    return{"message": "User deleted successfully"}

@router.get("/users", response_model=list[UserResponse])
def get_userss(skill: Optional[str] = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    if skill:
        query= db.query(User).filter(User.skills.like(f"%{skill}%")).offset(skip).limit(limit)
    else:
        query = db.query(User).offset(skip).limit(limit)
    users = query.all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    for user in users:
        user.skills = user.skills.split(",")
    return users

@router.get("/", response_model= list[UserResponse])
def get_users(sort_by : str = "age", order: str = "asc" ,db : Session = Depends(get_db)):
    allowed_sort_fields = ["age", "created_at"]
    if sort_by not in allowed_sort_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    if order == "desc":
        query= db.query(User).order_by(getattr(User, sort_by).desc())
    else:
        query = db.query(User).order_by(getattr(User, sort_by).asc())
    users = query.all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    for user in users:
        user.skills = user.skills.split(",")
    return users


