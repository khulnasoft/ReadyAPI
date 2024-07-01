from typing import Annotated

from readyapi import Query, ReadyAPI

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = None):
    if q is None:
        q = []
    query_items = {"q": q}
    return query_items
