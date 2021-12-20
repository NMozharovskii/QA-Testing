import requests

post_set_photo_headers = {
    "auth_key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "pet_id": "3abaef95-0811-44e4-9b43-b54091b45cd0",
    "name": "Mark2",
    "animal_type": "Ork",
    "age": '4',
    "pet_photo": ""

}

post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/my_pets/pet_photo/" + "3abaef95-0811-44e4-9b43-b54091b45cd0"


def post_set_photo(link, post_params, post_headers):
    response = requests.post(link, params=post_params, headers=post_headers, files={'pet_photo': open('Ishak.jpg', 'rb')})

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_set_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))
