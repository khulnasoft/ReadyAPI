import pytest
from readyapi.testclient import TestClient

from ...utils import needs_py39


@pytest.fixture(name="client")
def get_client():
    from docs_src.additional_status_codes.tutorial001_an_py39 import app

    client = TestClient(app)
    return client


@needs_py39
def test_update(client: TestClient):
    response = client.put("/items/foo", json={"name": "Wrestlers"})
    assert response.status_code == 200, response.text
    assert response.json() == {"name": "Wrestlers", "size": None}


@needs_py39
def test_create(client: TestClient):
    response = client.put("/items/red", json={"name": "Chillies"})
    assert response.status_code == 201, response.text
    assert response.json() == {"name": "Chillies", "size": None}
