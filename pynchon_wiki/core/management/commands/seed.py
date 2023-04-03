import logging

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db.models import Model

from core.factory import TopMenuFactory
from core.models import TopMenu
from users.factory import UserAdminFactory
from users.models import User
from wiki.factory import (BookFactory, ChapterFactory, ChapterLinkFactory,
                          CommentFactory, CommentLinkFactory,
                          TableChronologyFactory)
from wiki.models import (Chapter, Book, Comment, CommentLink, ChapterLink,
                         TableChronology)

logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Генерация тестовых данных'

    factories_and_generation_amount = {
        UserAdminFactory: 1,
        BookFactory: 5,
        ChapterFactory: 10,
        ChapterLinkFactory: 20,
        CommentFactory: 10,
        CommentLinkFactory: 20,
        TableChronologyFactory: 20,
        TopMenuFactory: 3,
    }

    models = (
        User, Book, Chapter, ChapterLink, Comment, CommentLink,
        TableChronology, TopMenu)

    def clean_db(self, models: [Model]):
        for model in models:
            try:
                model.objects.all().delete()
            except ObjectDoesNotExist:
                raise f'{model} не существует'

    def seed_data(self, factories: dict):
        for factory, amount in factories.items():
            for _ in range(amount):
                factory()

    def handle(self, *args, **options):
        self.clean_db(self.models)
        self.seed_data(self.factories_and_generation_amount)
