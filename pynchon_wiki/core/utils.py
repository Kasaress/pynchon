import bleach
import html

from django.shortcuts import get_object_or_404
import pymorphy2

from wiki.models import Book, Chapter


def load_chapters():
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapters = Chapter.objects.filter(book=book).order_by('sort')
    with open('test.doc', 'w') as f:
        for cptr in chapters:
            f.write(f'\nГлава {cptr.number}\n\n')
            for i in cptr.comments.all():
                f.write(
                    f'{i.name}\n\n'
                    f'Стр.{i.page_number_by_2012} / '
                    f'Стр.{i.page_number_by_2021}\n\n'
                    f'''{html.unescape(
                        bleach.clean(i.comment_text, strip=True))}\n\n'''
                )


def get_mounth_name(month_number, case='genitive'):
    months = {
        '01': 'январь',
        '02': 'февраль',
        '03': 'март',
        '04': 'апрель',
        '05': 'май',
        '06': 'июнь',
        '07': 'июль',
        '08': 'август',
        '09': 'сентябрь',
        '10': 'октябрь',
        '11': 'ноябрь',
        '12': 'декабрь',
    }

    month_name = months.get(month_number)
    if not month_name:
        return None

    morph = pymorphy2.MorphAnalyzer()
    parsed_word = morph.parse(month_name)[0]

    if case == 'genitive':
        return parsed_word.inflect({'gent'}).word

    return month_name
