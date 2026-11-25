from types import SimpleNamespace

import pytest
from pydantic import BaseModel

from src.baseclasses.response import Response


class Item(BaseModel):
    id: int
    name: str


def make_response(status_code=200, payload=None):
    return SimpleNamespace(
        status_code=status_code,
        json=lambda: payload if payload is not None else {"data": {"id": 1, "name": "Ada"}},
    )


def test_response_accepts_one_expected_status_code():
    wrapped = Response(make_response()).assert_status_code(200)

    assert wrapped.response_status == 200


def test_response_accepts_one_of_several_expected_status_codes():
    Response(make_response(status_code=204)).assert_status_code([200, 204])


def test_response_rejects_an_unexpected_status_code():
    with pytest.raises(AssertionError, match="does not match"):
        Response(make_response(status_code=500)).assert_status_code(200)


def test_response_validates_and_returns_one_object():
    wrapped = Response(make_response()).validate(Item)

    assert wrapped.get_parsed_object() == Item(id=1, name="Ada")


def test_response_validates_a_list_of_objects():
    wrapped = Response(
        make_response(payload={"data": [{"id": 1, "name": "Ada"}, {"id": 2, "name": "Lin"}]})
    ).validate(Item)

    assert wrapped.get_parsed_object() == [Item(id=1, name="Ada"), Item(id=2, name="Lin")]


def test_response_requires_a_data_field():
    wrapped = Response(make_response(payload={"meta": {}}))

    with pytest.raises(ValueError, match="'data' field"):
        wrapped.validate(Item)
