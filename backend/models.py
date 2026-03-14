from pydantic import BaseModel

class LostItem(BaseModel):
    item_name: str
    description: str
    location: str
    owner_name: str

class FoundItem(BaseModel):
    item_name: str
    description: str
    location: str
    finder_name: str