import pytest


@pytest.fixture()
@pytest.mark.django_db
def user_token(client, django_user_model):
    username = "mark2"
    password = "123"
    email = "mark2@example.com"
    role = "moderator"

    django_user_model.objects.create_user(
        username=username,
        password=password,
        email=email,
        role=role
    )
    response = client.post(
        "/users/token/",
        {"username": username, "password": password},
        format="json"
    )
    return response.json()["access"]
