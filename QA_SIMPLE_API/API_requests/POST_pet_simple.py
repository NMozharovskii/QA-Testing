import requests
# "key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff"


# POST PET SIMPLE
post_simple_headers = {
    "auth_key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "name": "Mark1",
    "animal_type": "unknown",
    "age": '8'
}

post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link, params=post_params, headers=post_headers)

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_params, post_simple_headers))

