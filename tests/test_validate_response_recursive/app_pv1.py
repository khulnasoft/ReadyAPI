from typing import List

from pydantic import BaseModel
from readyapi import ReadyAPI

app = ReadyAPI()


class RecursiveItem(BaseModel):
    sub_items: List["RecursiveItem"] = []
    name: str


RecursiveItem.update_forward_refs()


class RecursiveSubitemInSubmodel(BaseModel):
    sub_items2: List["RecursiveItemViaSubmodel"] = []
    name: str


class RecursiveItemViaSubmodel(BaseModel):
    sub_items1: List[RecursiveSubitemInSubmodel] = []
    name: str


RecursiveSubitemInSubmodel.update_forward_refs()


@app.get("/items/recursive", response_model=RecursiveItem)
def get_recursive():
    return {"name": "item", "sub_items": [{"name": "subitem", "sub_items": []}]}


@app.get("/items/recursive-submodel", response_model=RecursiveItemViaSubmodel)
def get_recursive_submodel():
    return {
        "name": "item",
        "sub_items1": [
            {
                "name": "subitem",
                "sub_items2": [
                    {
                        "name": "subsubitem",
                        "sub_items1": [{"name": "subsubsubitem", "sub_items2": []}],
                    }
                ],
            }
        ],
    }
