from pytest_factoryboy import register
from tests.factories import LocationFactory, UserFactory, CategoryFactory, AdFactory

pytest_plugins = ["tests.fixtures"]

register(LocationFactory)
register(UserFactory)
register(CategoryFactory)
register(AdFactory)
