import requests

# "key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff"

get_headers_my_pets = {
    "auth_key ": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "filter": "my_pets"
}

get_params_my_pets = get_headers_my_pets

my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


def get_pets_list(link, params, headers):
    response = requests.get(link, params=params, headers=headers)

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(get_pets_list(my_pets_link, get_params_my_pets, get_headers_my_pets))
