import pytest
import requests


from src.generators.player_loc import PlayerLoc

from src.schemas.computer import Computer
from examples import computer
from src.enamc.user_enums import Statuses



@pytest.mark.parametrize("status",Statuses.list())
def test_something(status, get_player_generator):
    print(get_player_generator.set_status(status).build())





@pytest.mark.parametrize("balance_value", [
    "100",
    "0",
    "-10",
    "asdasd",
])

def test_something1(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize("delete_key", [
    "account_status",
    "balance",
    "localize",
    "avatar",
])

def test_something2(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR")
])
def test_something3(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ["localize", localizations], PlayerLoc(loc).set_number(15).build()
    ).build()
    print(object_to_send)





def test_pydantic_object():
    comp = Computer.model_validate(computer)
    print(comp.schema_json())


# from src.baseclasses.response import Response
# from src.schemas.user import User
#
#
# def test_getting_users_list(get_users, make_number):
#     Response(get_users).assert_status_code(200).validate(User)
#     print(make_number)
#
#
# @pytest.mark.development
# @pytest.mark.production
# @pytest.mark.skip(reason="Not implemented")
# def test_another():
#     assert 1 == 1
#
#
# @pytest.mark.development
# @pytest.mark.production
# def test_another_failing_t():
#     """
#     In that test we try to check that 1 is equal to 2
#     """
#     assert 1 == 2
#
#
# @pytest.mark.development
# @pytest.mark.parametrize('first_value, second_value, result', [
#     (1, 2, 3),
#     (-1, -2, -3),
#     (-1, 2, 1),
#     ('b', -2, None),
#     ('b', 'b', None),
# ])
# def test_calculator(first_value, second_value, result, calculate):
#     """
#         In that test we testing calculating with different values(valid and invalid)
#     """
#     assert calculate(first_value, second_value) == result




## [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]
## https://my-json-server.typicode.com/typicode/demo/posts

#  z = {{
#     "meta": {
#         "pagination": {
#             "total": 2943,
#             "pages": 295,
#             "page": 1,
#             "limit": 10,
#             "links": {
#                 "previous": null,
#                 "current": "https://gorest.co.in/public/v1/users?page=1",
#                 "next": "https://gorest.co.in/public/v1/users?page=2"
#             }
#         }
#     },
#     "data": [
#         {
#             "id": 8470399,
#             "name": "Dhara Asan",
#             "email": "dhara_asan@osinski.test",
#             "gender": "female",
#             "status": "active"
#         },
#         {
#             "id": 8470398,
#             "name": "Sher Gupta",
#             "email": "gupta_sher@quigley-barrows.test",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 8470397,
#             "name": "Vedang Ganaka",
#             "email": "vedang_ganaka@hoeger.example",
#             "gender": "female",
#             "status": "inactive"
#         },
#         {
#             "id": 8470396,
#             "name": "Kama Dwivedi",
#             "email": "kama_dwivedi@thiel.example",
#             "gender": "female",
#             "status": "inactive"
#         },
#         {
#             "id": 8470395,
#             "name": "Dr. Lakshmi Ahluwalia",
#             "email": "dr_lakshmi_ahluwalia@hettinger-satterfield.example",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 8470394,
#             "name": "Gandharv Khanna",
#             "email": "gandharv_khanna@glover.test",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 8470393,
#             "name": "Ghanaanand Mehrotra",
#             "email": "ghanaanand_mehrotra@senger.test",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 8470392,
#             "name": "Abhaidev Kaul",
#             "email": "abhaidev_kaul@larkin.example",
#             "gender": "male",
#             "status": "inactive"
#         },
#         {
#             "id": 8470391,
#             "name": "Aagneya Iyengar",
#             "email": "iyengar_aagneya@medhurst.example",
#             "gender": "female",
#             "status": "active"
#         },
#         {
#             "id": 8470390,
#             "name": "Archan Kakkar",
#             "email": "kakkar_archan@barrows-stark.test",
#             "gender": "female",
#             "status": "active"
#         }
#     ]
# }