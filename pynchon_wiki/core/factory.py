from factory import django, Iterator, Faker

from core.models import TopMenu


class TopMenuFactory(django.DjangoModelFactory):
    class Meta:
        model = TopMenu

    name = Iterator(['Главная', 'О проекте', 'Войти'])
    url = Iterator(['/', '/about/', '/auth/login/'])
    sort = Faker('pyint', max_value=1000, step=100)
