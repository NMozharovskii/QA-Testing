import requests

delete_pet_headers = {
    "auth_key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "pet_id": "93802f43-bad7-428f-99df-8b72a14915e3"
}

delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "93802f43-bad7-428f-99df-8b72a14915e3"


def delete_pet(link, del_params, del_headers):
    response = requests.delete(link, params=del_params, headers=del_headers)

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(DELETE_pet_link, delete_pet_params, delete_pet_headers))
