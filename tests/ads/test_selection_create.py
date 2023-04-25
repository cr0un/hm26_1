import pytest
from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_token):
    # Создаем пользователя
    user_data = {
        "username": "mark2",
        "password": "123",
        "first_name": "name",
        "last_name": "surname",
        "role": "moderator",
        "birth_date": "2000-01-01",
        "email": "test12314545313@mail.ru",
        "locations": [
            {
                "name": "Тестовая локация",
                "lat": 11,
                "lng": 11
            }
        ]
    }

    user_response = client.post(
        "/users/create/",
        user_data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    # Создаем два объявления
    ad1 = AdFactory()
    ad2 = AdFactory()

    # Создаем подборку с использованием объявлений
    print(user_response.data)
    data = {
        "name": "Любимая подборка",
        "owner": 2,
        "items": [ad1.id, ad2.id]
    }

    response = client.post(
        "/selection/",
        data,
        content_type="application/json",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    # Ожидаемый ответ
    expected_response = {
        "id": response.data["id"],
        "owner": "mark2",
        "name": "Любимая подборка",
        "items": [
            ad1.id,
            ad2.id
        ]
    }

    # Проверка
    assert response.data == expected_response
