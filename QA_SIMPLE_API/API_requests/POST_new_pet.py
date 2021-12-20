import requests

post_new_pet_headers = {
    "auth_key": "9d09379b8221290e8fc2cab87e55e2a580e5acda4d8222cfd20b2eff",
    "name": "Mark2",
    "animal_type": "Ork",
    "age": '4',
    "pet_photo": ""
}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link, params=post_params, headers=post_headers, files={"pet_photo": open('shrek.jpg', 'rb')})

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))
