from pymongo import MongoClient
import os
Mongo_url=os.getenv("Mongo_url","mongodb://localhost27017")

Client =MongoClient(Mongo_url)
db=Client["login_app"]
user_collection=db["users"]
