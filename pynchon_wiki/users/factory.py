from django.contrib.auth.hashers import make_password
from factory import Faker, django

from users.models import User


class UserAdminFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    username = 'admin'
    email = 'test@admin.ru'
    password = make_password('admin')
    is_staff = True
    is_superuser = True
