from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Item
import os


from lastFM import get_similiar_artists, get_corrected_artists, get_similiar_tracks, get_corrected_tracks

# from database_f import fetch_all_items, fetch_one_item, create_item, update_item, remove_item
# app object
app = FastAPI()

#CORS

origins = [
    "http://localhost:3000",
    "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/get_correct_artist")
def get_corrected_artist():
    return get_corrected_artists()

# get items
@app.get("/api/get_items")
async def get_items():
    return 1
    

@app.post("/api/post_item")
async def post_data(item: Item):
    return (f"Got this {item.name}!") 

# put data
@app.put("/api/put_item/{id}")
async def put_data(id,item):
    return 1

# delete data
@app.delete("/api/delete_item/{id}")
async def delete_data(id):
    return 1