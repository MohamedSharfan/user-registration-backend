# from fastapi import FastAPI, Depends, HTTPException, status
# from  fastapi.security import OAuth2PasswordRequestForm
# from security import hash_password, verify_password, create_access_token

# app = FastAPI()

# fake_db={}

# @app.post("/signup")
# async def signup(username: str, password: str):
#     if username in fake_db:
#         raise HTTPException(status_code=400, detail="user already exists")
#     hashed = hash_password(password)
#     fake_db[username] = {"username": username, "password": hashed}
#     return {"msg": "User Created"}

# @app.post("/login")
# async def login(form_data : OAuth2PasswordRequestForm= Depends()):
#     user = fake_db.get(form_data.username)
#     if not user or not verify_password(form_data.password, user["password"]):
#         raise HTTPException(status_code=401, detail="Invalid credintial")
    
#     token = create_access_token(data = {"sub": user["username"]})
#     return {"access_token": token, "type": "bearer"}


from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from security import hash_password, verify_password, create_access_token

app = FastAPI()

# 1. Start with an empty DB (Don't hardcode plaintext passwords!)
fake_db = {} 

@app.post("/signup")
async def signup(username: str, password: str):
    if username in fake_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed = hash_password(password)
    
    # 2. FIX: Use the 'username' variable as the key, NOT the string 'username'
    fake_db[username] = {"username": username, "password": hashed}
    
    # Debug print to prove it worked
    print(f"User created! DB is now: {fake_db}")
    return {"msg": "User Created"}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 3. This looks for the KEY 'sharfan' in the dictionary
    user = fake_db.get(form_data.username)
    
    if not user:
        print(f"User {form_data.username} not found in DB.")
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
    if not verify_password(form_data.password, user["password"]):
        print("Password mismatch")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}