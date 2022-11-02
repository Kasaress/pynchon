import csv
import os.path
import sys

from django.core.management.base import BaseCommand

from wiki.models import TableChronology


class Command(BaseCommand):
    help = ('Import CSV-file into the base. '
            'Use command: python manage.py BASE FILE.CSV'
            )
    BASES = {
        'table': TableChronology,
    }

    def handle(self, *args, **options):
        if len(args) < 2:
            sys.exit(
                'Too low arguments! Usage: python manage.py base file.csv')
        if args[0].lower() not in self.BASES:
            sys.exit(
                f'Base unknown. Known bases are: {list(self.BASES.keys())}')
        if not os.path.exists(args[1]):
            sys.exit(
                f'File {args[1]} not exists!')
        base = self.BASES[args[0].lower()]
        with open(args[1], 'r', encoding="utf-8") as csvfile:
            try:
                # reader = csv.DictReader(csvfile, delimiter=";")
                reader = csv.reader(csvfile, delimiter=";")
            except Exception as e:
                sys.exit(f'CSV-file read exception {e}')
            writed_rows = 0
            for row in reader:
                try:
                    print(row)
                    base(*row).save()
                except Exception as e:
                    print(f'Exception {e}')
                else:
                    writed_rows += 1
                finally:
                    print(
                        f'Added {writed_rows} rows to base {args[0].lower()}'
                    )

    def add_arguments(self, parser):
        parser.add_argument(
            nargs='+',
            type=str,
            dest='args'
        )