from pydantic import ValidationError
import pytest

from src.enamc.user_enums import Genders, Statuses
from src.pydantic_schemas.post import Post
from src.schemas.computer import Computer
from src.schemas.user import User


COMPUTER_EXAMPLE = {
    "id": 21,
    "status": "ACTIVE",
    "activated_at": "2013-06-01",
    "expiration_at": "2040-06-01",
    "host_v4": "91.192.222.17",
    "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "detailed_info": {
        "physical": {
            "color": "green",
            "photo": "https://example.com/computer.png",
            "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c",
        },
        "owners": [
            {
                "name": "Stephan Nollan",
                "card_number": "4000000000000002",
                "email": "stephan@example.com",
            }
        ],
    },
}


def test_user_accepts_valid_data_and_normalizes_status_case():
    """Проверяет валидного пользователя и приведение статуса к элементу перечисления."""
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
    """Проверяет отклонение некорректного email, имени, пола или статуса."""
    data = {"id": 1, "name": "Ada", "email": "ada@example.com", "gender": "female", "status": "active"}
    data.update(changes)

    with pytest.raises(ValidationError):
        User.model_validate(data)


def test_computer_example_matches_nested_schema():
    """Проверяет валидацию учебного примера компьютера и вложенных объектов."""
    result = Computer.model_validate(COMPUTER_EXAMPLE)

    assert result.id == COMPUTER_EXAMPLE["id"]
    assert result.detailed_info.owners[0].email == "stephan@example.com"


def test_computer_rejects_an_invalid_ip_address():
    """Проверяет, что схема компьютера отклоняет неверный IPv4-адрес."""
    data = {**COMPUTER_EXAMPLE, "host_v4": "not-an-ip"}

    with pytest.raises(ValidationError):
        Computer.model_validate(data)


def test_post_accepts_ids_up_to_two():
    """Проверяет, что модель публикации принимает ID, равный двум."""
    assert Post.model_validate({"id": 2, "title": "Example"}).id == 2


def test_post_rejects_ids_above_two():
    """Проверяет, что модель публикации отклоняет ID больше двух."""
    with pytest.raises(ValidationError, match="ID must be less than 2"):
        Post.model_validate({"id": 3, "title": "Example"})
