from typing import Optional

from pydantic import BaseModel
from readyapi import Depends, ReadyAPI, Security
from readyapi.security.open_id_connect_url import OpenIdConnect
from readyapi.testclient import TestClient

app = ReadyAPI()

oid = OpenIdConnect(openIdConnectUrl="/openid", auto_error=False)


class User(BaseModel):
    username: str


def get_current_user(oauth_header: Optional[str] = Security(oid)):
    if oauth_header is None:
        return None
    user = User(username=oauth_header)
    return user


@app.get("/users/me")
def read_current_user(current_user: Optional[User] = Depends(get_current_user)):
    if current_user is None:
        return {"msg": "Create an account first"}
    return current_user


client = TestClient(app)


def test_security_oauth2():
    response = client.get("/users/me", headers={"Authorization": "Bearer footokenbar"})
    assert response.status_code == 200, response.text
    assert response.json() == {"username": "Bearer footokenbar"}


def test_security_oauth2_password_other_header():
    response = client.get("/users/me", headers={"Authorization": "Other footokenbar"})
    assert response.status_code == 200, response.text
    assert response.json() == {"username": "Other footokenbar"}


def test_security_oauth2_password_bearer_no_header():
    response = client.get("/users/me")
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Create an account first"}


def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == {
        "openapi": "3.1.0",
        "info": {"title": "ReadyAPI", "version": "0.1.0"},
        "paths": {
            "/users/me": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "Successful Response",
                            "content": {"application/json": {"schema": {}}},
                        }
                    },
                    "summary": "Read Current User",
                    "operationId": "read_current_user_users_me_get",
                    "security": [{"OpenIdConnect": []}],
                }
            }
        },
        "components": {
            "securitySchemes": {
                "OpenIdConnect": {
                    "type": "openIdConnect",
                    "openIdConnectUrl": "/openid",
                }
            }
        },
    }
