from readyapi import ReadyAPI
from readyapi.testclient import TestClient

app = ReadyAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    if response.status_code != 200:
        raise AssertionError
    if response.json() != {"msg": "Hello World"}:
        raise AssertionError
