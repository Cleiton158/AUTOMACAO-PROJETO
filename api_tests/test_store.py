import requests

BASE_URL = "https://petstore.swagger.io/v2"

order_id = 12345


def test_create_order():

    payload = {
        "id": order_id,
        "petId": 99999,
        "quantity": 1,
        "shipDate": "2025-05-07T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }

    response = requests.post(f"{BASE_URL}/store/order", json=payload)

    assert response.status_code == 200


def test_get_order():

    response = requests.get(f"{BASE_URL}/store/order/{order_id}")

    assert response.status_code == 200

    response_body = response.json()

    assert response_body["id"] == order_id


def test_delete_order():

    response = requests.delete(f"{BASE_URL}/store/order/{order_id}")

    assert response.status_code == 200