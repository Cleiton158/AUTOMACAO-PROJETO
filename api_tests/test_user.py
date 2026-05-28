import requests

BASE_URL = "https://petstore.swagger.io/v2"

pet_id = 99999


def test_create_pet():

    payload = {
        "id": pet_id,
        "name": "Bolt",
        "status": "available"
    }

    response = requests.post(f"{BASE_URL}/pet", json=payload)

    assert response.status_code == 200


def test_get_pet():

    response = requests.get(f"{BASE_URL}/pet/{pet_id}")

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["name"] == "Bolt"


def test_delete_pet():

    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")

    assert response.status_code == 200