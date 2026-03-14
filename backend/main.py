from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import LostItem, FoundItem
from database import lost_collection, found_collection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Lost and Found API Running"}


@app.post("/lost")
def report_lost(item: LostItem):
    lost_collection.insert_one(item.model_dump())
    return {"message": "Lost item reported"}


@app.post("/found")
def report_found(item: FoundItem):
    found_collection.insert_one(item.model_dump())

    match = lost_collection.find_one({
        "item_name": item.item_name,
        "location": item.location
    })

    if match:
        match.pop("_id")
        return {
            "message": "Possible match found",
            "lost_item": match
        }

    return {"message": "Found item reported"}


@app.get("/lost-items")
def get_lost_items():
    items = []

    for item in lost_collection.find():
        item.pop("_id")
        items.append(item)

    return items


@app.get("/found-items")
def get_found_items():
    items = []

    for item in found_collection.find():
        item.pop("_id")
        items.append(item)

    return items