from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from routes.users import get_db
from schemas import ProductCreate, ProductResponse
from models import Product
from dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db), user = Depends(get_current_user)):
    db_product = Product(**product.dict(), owner_id=user["user_id"])
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/items")
async def read_items(db: Session = Depends(get_db),skip: int = 0, limit: int = 10):
    users = db.query(Product).offset(skip).limit(limit).all()
    if not users:
        raise HTTPException(status_code = 404, detail="user not found")
    return users


@router.delete("/items/{item_id}")
def delete_item(item_id : int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == item_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.owner_id != user["user_id"]:
        raise HTTPException(status_code=403, detail="Forbidden")
    db.delete(product)
    db.commit()
    return{"messege": "successfully deleted"}
