from typing import List

import pytest
from readyapi import ReadyAPI
from readyapi.exceptions import ReadyAPIError


class NonPydanticModel:
    pass


def test_invalid_response_model_raises():
    with pytest.raises(ReadyAPIError):
        app = ReadyAPI()

        @app.get("/", response_model=NonPydanticModel)
        def read_root():
            pass  # pragma: nocover


def test_invalid_response_model_sub_type_raises():
    with pytest.raises(ReadyAPIError):
        app = ReadyAPI()

        @app.get("/", response_model=List[NonPydanticModel])
        def read_root():
            pass  # pragma: nocover


def test_invalid_response_model_in_responses_raises():
    with pytest.raises(ReadyAPIError):
        app = ReadyAPI()

        @app.get("/", responses={"500": {"model": NonPydanticModel}})
        def read_root():
            pass  # pragma: nocover


def test_invalid_response_model_sub_type_in_responses_raises():
    with pytest.raises(ReadyAPIError):
        app = ReadyAPI()

        @app.get("/", responses={"500": {"model": List[NonPydanticModel]}})
        def read_root():
            pass  # pragma: nocover
