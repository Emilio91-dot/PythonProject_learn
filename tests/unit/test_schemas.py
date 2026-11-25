from pydantic import ValidationError
import pytest

from examples import computer
from src.enamc.user_enums import Genders, Statuses
from src.pydantic_schemas.post import Post
from src.schemas.computer import Computer
from src.schemas.user import User


def test_user_accepts_valid_data_and_normalizes_status_case():
    user = User.model_validate(
        {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com", "gender": "female", "status": "ACTIVE"}
    )

    assert user.name == "Ada Lovelace"
    assert user.gender is Genders.FEMALE
    assert user.status is Statuses.ACTIVE


@pytest.mark.parametrize(
    "changes",
    [
        {"email": "not-an-email"},
        {"name": 42},
        {"gender": "unknown"},
        {"status": "unknown"},
    ],
)
def test_user_rejects_invalid_field_values(changes):
    data = {"id": 1, "name": "Ada", "email": "ada@example.com", "gender": "female", "status": "active"}
    data.update(changes)

    with pytest.raises(ValidationError):
        User.model_validate(data)


def test_computer_example_matches_nested_schema():
    result = Computer.model_validate(computer)

    assert result.id == computer["id"]
    assert result.detailed_info.owners[0].email == computer["detailed_info"]["owners"][0]["email"]


def test_computer_rejects_an_invalid_ip_address():
    data = {**computer, "host_v4": "not-an-ip"}

    with pytest.raises(ValidationError):
        Computer.model_validate(data)


def test_post_accepts_ids_up_to_two():
    assert Post.model_validate({"id": 2, "title": "Example"}).id == 2


def test_post_rejects_ids_above_two():
    with pytest.raises(ValidationError, match="ID must be less than 2"):
        Post.model_validate({"id": 3, "title": "Example"})
