from fastapi import FastAPI
from database import Base, engine
from routes.users import router as users_router, auth_router
from routes.products import router as products_router


Base.metadata.create_all(bind = engine)

app = FastAPI()

# Register authentication routes at root level
app.include_router(auth_router, tags=["Authentication"])

# Register user routes
app.include_router(users_router, prefix="/users", tags=["Users"])

app.include_router(products_router, prefix="/products", tags=["Products"])