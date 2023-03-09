import logging

from django.core.management.base import BaseCommand
from django.db.models import Model

from users.factory import UserAdminFactory
from users.models import User

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    factories_and_generation_amount = {
        UserAdminFactory: 1,
    }

    models = (User,)

    def clean_db(self, models: [Model]):
        for model in models:
            try:
                model.objects.all().delete()
            except Model.DoesNotExist:
                raise f'{model} не существует'

    def seed_data(self, factories: dict):
        for factory, amount in factories.items():
            for _ in range(amount):
                factory()

    def handle(self, *args, **options):
        self.clean_db(self.models)
        self.seed_data(self.factories_and_generation_amount)
