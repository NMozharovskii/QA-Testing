import pytest
import requests

# ПАРАМЕТРЫ

# POST PET SIMPLE
post_simple_headers = {
    "auth_key ": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "name": "Pinki",
    "animal_type": "Rat",
    "age": '6'
}
post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"

# API KEY
get_key_headers = {
    "email": "qwerty@mail.ru",
    "password": "qwerty123"
}
get_key_params = get_key_headers
api_key_link = "https://petfriends1.herokuapp.com/api/key"

# PETS LIST
get_headers_my_pets = {
    "auth_key ": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "filter": "my_pets"
}
get_params_my_pets = get_headers_my_pets
my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"

# NEW PET
post_new_pet_headers = {
    "auth_key ": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "name": "Brain",
    "animal_type": "Big Head Rat",
    "age": '8',
    "pet_photo": ""
}
post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"

# DELETE
delete_pet_headers = {
    "auth_key ": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "pet_id": "76b2d780-861f-45cb-a40c-ec60d948d391"
}
delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "76b2d780-861f-45cb-a40c-ec60d948d391"

# PUT INFO
put_info_headers = {
    "auth_key ": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "pet_id": "3abaef95-0811-44e4-9b43-b54091b45cd0"
}
put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "3abaef95-0811-44e4-9b43-b54091b45cd0"


# ФИКСТУРЫ
@pytest.fixture
def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link, params=post_params, headers=post_headers)
    return response.ok


@pytest.fixture
def get_api_key(link, params, headers):
    response = requests.get(link, params=params, headers=headers)
    if response.status_code == 200:
        return True


@pytest.fixture
def get_pets_list(link, params, headers):
    response = requests.get(link, params=params, headers=headers)
    if response.status_code == 200:
        return True


@pytest.fixture
def post_new_pet(link, post_params, post_headers):
    response = requests.post(link, params=post_params, headers=post_headers, files={"pet_photo": open('BrainRat.jpeg', 'rb')})
    return response.ok


@pytest.fixture
def delete_pet(link, del_params, del_headers):
    response = requests.delete(link, params=del_params, headers=del_headers)
    if response.status_code == 200:
        return True


@pytest.fixture
def put_pet_info():
    response = requests.put(put_info_link, params=put_info_params, headers=put_info_headers)
    return response.ok



# ТЕСТЫ
@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (create_pet_simple_POST_link, post_simple_params, post_simple_headers, True),

                             (new_pet_POST_link, post_new_pet_params, post_new_pet_headers, False),
                         ])
def test_post(link, params, header, expected_result):
    response = requests.post(link, params=params, headers=header)
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (api_key_link, get_key_params, get_key_headers, True),

                             (my_pets_link, get_params_my_pets, get_headers_my_pets, True)
                         ])
def test_get(link, params, header, expected_result):
    response = requests.get(link, params=params, headers=header)
    assert response.ok == expected_result


@pytest.mark.parametrize('link, params, header, expected_result',
                         [
                             (DELETE_pet_link, delete_pet_params, delete_pet_headers, True)
                         ])
def test_delete(link, params, header, expected_result):
    response = requests.delete(link, params=params, headers=header)
    assert response.ok == expected_result


def test_put(put_pet_info):
    assert put_pet_info == True
