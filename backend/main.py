# from fastapi import FastAPI,HTTPException
# from models import loginuser
# from database import user_collection
# from fastapi.middleware.cors import CORSMiddleware
# from auth import verify_password, hash_password

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # restrict later
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/login")
# def login(user: loginuser):
#     db_user = user_collection.find_one({"email": user.email})

#     if not db_user:
#         raise HTTPException(status_code=401, detail="User not found")

#     if not verify_password(user.password, db_user["password"]):
#         raise HTTPException(status_code=401, detail="Invalid password")

#     return {"message": "Login successful ✅"}
# @app.post("/signup")
# def signup(user: loginuser):
#     existing_user = user_collection.find_one({"email": user.email})

#     if existing_user:
#         raise HTTPException(status_code=400, detail="User already exists")

#     user_collection.insert_one({
#         "email": user.email,
#         "password": hash_password(user.password)
#     })

#     return {"message": "User registered successfully ✅"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from pymongo import MongoClient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["login_app"]
collection = db["login_data"]

class LoginData(BaseModel):
    email: EmailStr
    password: str

@app.post("/login")
def store_login(data: LoginData):
    collection.insert_one({
        "email": data.email,
        "password": data.password
    })

    return {"message": "Data stored successfully (❁´◡`❁)"}
from bson import ObjectId

@app.get("/logins")
def get_all_logins():
    data = []
    for item in collection.find():
        data.append({
            "id": str(item["_id"]),
            "email": item["email"],
            "password": item["password"]
        })
    return data
