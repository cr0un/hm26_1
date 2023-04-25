import pytest


@pytest.mark.django_db
def test_retrieve_ad(client, ad, user_token):
    expected_response = {
        "id": ad.pk,
        "name": "test123445",
        "author": ad.author_id,
        "price": 999,
        "description": "",
        "is_published": False,
        # "category": 1,
        "category": ad.category_id,
        "image": None,
        "location": {
            "name": ad.location.name,
            "lat": ad.location.lat,
            "lng": ad.location.lng
        }
    }

    response = client.get(
        f"/ads/{ad.pk}/",
        HTTP_AUTHORIZATION="Bearer " + user_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
