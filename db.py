from pymongo import MongoClient
import os

# MongoDB configuration
client = MongoClient(os.getenv("MONGO_URI"))
db = client["reaction_bot_db"]
users_collection = db["users"]

# Function to store a new user in the database
def store_new_user(user_id, username):
    users_collection.insert_one({"user_id": user_id, "username": username})

# Function to fetch all users
def get_all_users():
    return users_collection.find()

# Function to log reactions
def log_reaction(user_id, reaction):
    users_collection.update_one(
        {"user_id": user_id},
        {"$push": {"reactions": reaction}},
        upsert=True
    )
