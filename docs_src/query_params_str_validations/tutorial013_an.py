from readyapi import Query, ReadyAPI
from typing_extensions import Annotated

app = ReadyAPI()


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = None):
    if q is None:
        q = []
    query_items = {"q": q}
    return query_items
