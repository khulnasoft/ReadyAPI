from pydantic import BaseModel
from readyapi import ReadyAPI
from readyapi.responses import JSONResponse


class Item(BaseModel):
    id: str
    value: str


class Message(BaseModel):
    message: str


app = ReadyAPI()


@app.get("/items/{item_id}", response_model=Item, responses={404: {"model": Message}})
async def read_item(item_id: str):
    if item_id == "foo":
        return {"id": "foo", "value": "there goes my hero"}
    return JSONResponse(status_code=404, content={"message": "Item not found"})
