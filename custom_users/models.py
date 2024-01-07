from django.db import models
from django.contrib.auth.models import User


GENDER_TYPE = (
    ("MALE", "M"),
    ("FEMALE", 'Ж'),
    ('UNDEFINED', 'Нет')
)

CITY_TYPE = (
    ("KG", "Кыргызстан"),
    ("KZ", "Казахстан"),
    ("RUS", "Россия"),
    ("USA", "Америка"),
    ("CN", "Китай"),
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13, default='+996',
                                    verbose_name='Укажите номер телефона')
    date_of_birth = models.DateField(verbose_name='Ваша дата рождения?')
    gender = models.CharField(max_length=100, null=True, choices=GENDER_TYPE,
                              verbose_name='Ваш пол')
    city = models.CharField(max_length=100, null=True, choices=CITY_TYPE,
                            verbose_name='Ваша страна')
