import pytest

@pytest.mark.django_db
def test_ad_create(client, ad, user_token):
    user_data = {
        "username": "user123131454534",
        "password": "password",
        "first_name": "name",
        "last_name": "surname",
        "role": "moderator",
        "birth_date": "2000-01-01",
        "email": "test12314545313@mail.ru",
        # "locations": [location_data]
        "locations": {
            "name": "Тестовая локация",
            "lat": 11,
            "lng": 11
        }
    }

    user_response = client.post(
        "/users/create/",
        user_data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    # location = user_response.data["locations"]

    # Создаем объявление с использованием объекта локации
    data = {
            "name": "test123445",
            "author": ad.author_id,
            "price": 999,
            "description": "",
            "is_published": False,
            "category": 1,
            "locations": {
                "name": "Тестовая локация",
                "lat": 11,
                "lng": 11
            }
    }

    response = client.post(
        "/ads/create/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    # Ожидаемый ответ
    expected_response = {
        "id": response.data["id"],
        "name": "test123445",
        "author": ad.author_id,
        "price": 999,
        "description": "",
        "is_published": False,
        "category": 1,
        "image": None,
        "location": {
            "name": "",
            "lat": None,
            "lng": None
        }
    }

    # Проверка
    assert response.data == expected_response

