import requests

put_info_headers = {
    "auth_key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "pet_id": "3abaef95-0811-44e4-9b43-b54091b45cd0",
    "name": "Mark1",
    "animal_type": "Ishak",
    "age": '8'

}

put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "3abaef95-0811-44e4-9b43-b54091b45cd0"


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link, params=p_params, headers=p_headers)

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))
