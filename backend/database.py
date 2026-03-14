from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["lost_found_db"]

lost_collection = db["lost_items"]
found_collection = db["found_items"]