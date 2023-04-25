import factory
from faker.utils.text import slugify

from ads.models import Ad, Category, Selection
from users.models import User, Location


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    name = "Тестовая локация"
    lat = 11
    lng = 11


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
    age = 20
    birth_date = "2003-01-01"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    slug = factory.LazyAttribute(lambda obj: slugify(obj.name))


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "test123445"
    author = factory.SubFactory(UserFactory)
    price = 999
    description = ""
    is_published = False
    image = None
    category = factory.SubFactory(CategoryFactory)
    location = factory.SubFactory(LocationFactory)


class SelectionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Selection

    name = "Любимая подборка"
    owner = factory.SubFactory(UserFactory)
    # items = factory.RelatedFactoryList(AdFactory, size=2)
    items = factory.List([factory.SubFactory(AdFactory) for _ in range(2)])