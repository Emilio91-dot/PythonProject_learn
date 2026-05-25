import requests


from src.baseclasses.response import Response
from src.schemas.user import User



def test_getting_users_list(get_users, make_number):
   Response(get_users).assert_status_code(200).validate(User)
   print('make_number')


def test_another():
    assert 1 == 1




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