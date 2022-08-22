from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    number: int


@app.post("/items")
def create_item(item: Item):
    return item