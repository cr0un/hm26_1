from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


def validate_email_domain(value):
    if "rambler.ru" in value:
        raise ValidationError("Регистрация с почтового адреса в домене rambler.ru запрещена.")


def validate_birth_date(value):
    now = date.today()
    age = now.year - value.year - ((now.month, now.day) < (value.month, value.day))

    if age < 9:
        raise ValidationError("Пользователям младше 9 лет регистрация запрещена.")


class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    lat = models.FloatField(verbose_name="Широта")
    lng = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    STATUS = [
        (MEMBER, "Гость"),
        (MODERATOR, "Модератор"),
        (ADMIN, "Администратор")
    ]
    role = models.CharField(max_length=9, verbose_name="Роль", default="member", choices=STATUS)
    age = models.PositiveSmallIntegerField(null=True, verbose_name="Возраст")
    locations = models.ManyToManyField(Location, verbose_name="Локация")
    birth_date = models.DateField(null=True, verbose_name="Дата рождения", validators=[validate_birth_date])
    email = models.EmailField(verbose_name="Электронная почта", validators=[
        validate_email_domain])

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



