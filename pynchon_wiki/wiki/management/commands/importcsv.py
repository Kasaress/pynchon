import csv
import os.path
import sys
from django.conf import settings
from django.core.management.base import BaseCommand

from wiki.models import TableChronology, Comment

class Command(BaseCommand):
    help = ('Import CSV-files. Use command: python3 manage.py importcsv')
    BASES = {
        # 'ingredients': Ingredient,
        'Comment': Comment,
    }
    FILES = {
        'Comment': '/Users/yanabubnova/DEV/pynchon/pynchon_wiki/wiki/static/data/test_comments.csv',
        # 'tags': f'{settings.DATA_ROOT}/tags.csv',
    }

    def _get_or_create_object(self, model, data):
        if model == Comment:
            return model.objects.get_or_create(
                                origin_text=data['origin_text'],
                                comment_text=data['comment_text'],
                                links=data['links'],
                                image=data['image'],
                                book_id=1,
                                chapter_id=data['chapter'],
                                page_number_by_2012=data['page_number_by_2012'],
                                page_number_by_2021=data['page_number_by_2021'],
                                order_number=data['order_number'],
                                author_id=1,
                            )
        # return model.objects.get_or_create(
        #                     name=data['name'].lower(),
        #                     measurement_unit=data['measurement_unit']
        #                 )

    def handle(self, *args, **options):
        for base_name, base in self.BASES.items():
            with open(self.FILES[base_name], 'r', encoding="utf-8") as csvfile:
                try:
                    reader = csv.DictReader(csvfile, delimiter=',')
                except Exception as e:
                    sys.exit(f'CSV-file read exception {e}')
                for row in reader:
                    try:
                        new_obj, status = self._get_or_create_object(base, row)
                        if status:
                            print(
                                f'Создан новый объект: "{new_obj}"'
                            )
                        else:
                            print(
                                f'Объект "{new_obj}" создан ранее'
                            )
                    except Exception as e:
                        print(f'Exception {e}')
# class Command(BaseCommand):
#     help = ('Import CSV-file into the base. '
#             'Use command: python manage.py BASE FILE.CSV'
#             )
#     BASES = {
#         'table': TableChronology,
#         'comments': Comment,
#     }

#     def handle(self, *args, **options):
#         if len(args) < 2:
#             sys.exit(
#                 'Too low arguments! Usage: python manage.py base file.csv')
#         if args[0].lower() not in self.BASES:
#             sys.exit(
#                 f'Base unknown. Known bases are: {list(self.BASES.keys())}')
#         if not os.path.exists(args[1]):
#             sys.exit(
#                 f'File {args[1]} not exists!')
#         base = self.BASES[args[0].lower()]
#         with open(args[1], 'r', encoding="utf-8") as csvfile:
#             try:
#                 # reader = csv.DictReader(csvfile, delimiter=";")
#                 reader = csv.reader(csvfile, delimiter=";")
#             except Exception as e:
#                 sys.exit(f'CSV-file read exception {e}')
#             writed_rows = 0
#             for row in reader:
#                 try:
#                     print(row)
#                     base(*row).save()
#                 except Exception as e:
#                     print(f'Exception {e}')
#                 else:
#                     writed_rows += 1
#                 finally:
#                     print(
#                         f'Added {writed_rows} rows to base {args[0].lower()}'
#                     )

#     def add_arguments(self, parser):
#         parser.add_argument(
#             nargs='+',
#             type=str,
#             dest='args'
#         )