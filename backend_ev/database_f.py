from model import Item
from database import engine, SessionLocal, Base
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://localhost:27017')

db = client.Items
collection = db.shop

async def fetch_one_item(id):
    document = await collection.find_one({"id": id})
    return document

async def fetch_all_items():
    item_collection = []
    cursor = collection.find()
    async for document in cursor:
        item_collection.append(Item(**document))
    return item_collection
     

async def create_item(item):
    document = item
    result = await collection.insert_one(document)
    return result

async def update_item(id, name,price):
    await collection.update_one({"id": id}, {"$set": {"name": name, "price": price}})
    doc = await collection.find_one({"id": id})
    return doc

async def remove_item(id):
    await collection.delete_one({"id": id})
    return True
    