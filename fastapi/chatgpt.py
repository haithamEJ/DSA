from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = [Item(text="haitham", is_done=True), Item(text="hatim")]

@app.get("/")
def root():
    return {"Hello":"World"}

@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return {"message": "Item added", "item": item}


@app.get("/items/{item_id}")
def get_item(item_id:int) -> Item:
    if item_id < len(items):
       return items[item_id]
    else :
        raise HTTPException(status_code=404, detail="Item not found")