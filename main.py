from typing import Optional
from test import FastAPI,Query
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name:str
    price:float
    is_offer:Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello":"World"}
@app.get("/items/{item_id}")
def read_item(item_id: int, q:Optional[str] = None):
    return {"item_id":item_id,"q":q}
@app.put("/items/{item_id}")
def update_item(item_id:int, item:Item):
    result = item_id  if item_id else item
    return {
        "item_name":item.name,
        "item_id":item_id
    }
@app.get("/items")
async def read_items(q:Optional[str]= Query(None,max_length=50)):
    results = {"items":[{"item_id":"Foo"}]}