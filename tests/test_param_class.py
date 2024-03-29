from typing import Optional

from readyapi import ReadyAPI
from readyapi.params import Param
from readyapi.testclient import TestClient

app = ReadyAPI()


@app.get("/items/")
def read_items(q: Optional[str] = Param(default=None)):  # type: ignore
    return {"q": q}


client = TestClient(app)


def test_default_param_query_none():
    response = client.get("/items/")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": None}


def test_default_param_query():
    response = client.get("/items/?q=foo")
    assert response.status_code == 200, response.text
    assert response.json() == {"q": "foo"}
