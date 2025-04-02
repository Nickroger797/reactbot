from pymongo import MongoClient
import os

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["reaction_bot_db"]
users_collection = db["users"]

# Function to store a new user in the database (Avoids duplicates)
def store_new_user(user_id, username):
    if not users_collection.find_one({"user_id": user_id}):  # Check if user already exists
        users_collection.insert_one({"user_id": user_id, "username": username, "reactions": []})

# Function to fetch all users as a list
def get_all_users():
    return list(users_collection.find({}, {"_id": 0}))  # Excludes MongoDB `_id`

# Function to log reactions (Ensures user exists before adding reaction)
def log_reaction(user_id, reaction):
    users_collection.update_one(
        {"user_id": user_id},
        {"$setOnInsert": {"username": None, "reactions": []}, "$push": {"reactions": reaction}},
        upsert=True
    )
