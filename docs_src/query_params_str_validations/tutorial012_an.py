from typing import List

from readyapi import Query, ReadyAPI
from typing_extensions import Annotated

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: Annotated[List[str], Query()] = None):
    if q is None:
        q = ["foo", "bar"]
    query_items = {"q": q}
    return query_items
