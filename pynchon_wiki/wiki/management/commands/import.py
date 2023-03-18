import os.path
from csv import DictReader

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand

# Импорт моделей
from wiki.models import (Book, Chapter, ChapterLink, Comment, CommentLink,
                         TableChronology)

User = get_user_model()


class Command(BaseCommand):
    help = "Команда для загрузки тестовых данных в БД из csv файлов"

    # Список переменных для импорта данных в модели
    models = (
        (
            (Book, 'books'),
            (Chapter, 'chapters'),
            (Comment, 'comments'),
        ),
    )

    def clean_db(self):
        for data in self.models:
            for model, file in data:
                try:
                    model.objects.all().delete()
                except ObjectDoesNotExist:
                    raise f'{model} не существует'

    def import_data(self):
        """ Метод импортирует пользователей, книги и т.д. в БД. """

        for data in self.models:
            for model, file in data:
                with open(f'{settings.BASE_DIR}/static/data/{file}.csv',
                          encoding='utf-8') as f:
                    print(f'Начался импорт данных {file}')
                    for row in DictReader(f):
                        if not model.objects.filter(**row).exists():
                            model.objects.create(**row)
                print(f'Импорт данных {file} завершен.')

    def handle(self, *args, **options):
        """ Агрегирующий метод, который вызывается с помощью команды import
        и добавляет тестовые данные в БД. """

        self.clean_db()
        self.import_data()
