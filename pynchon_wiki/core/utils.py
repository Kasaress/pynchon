import bleach
import html

from django.shortcuts import get_object_or_404

from wiki.models import Book, Chapter


def load_chapters():
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapters = Chapter.objects.filter(book=book)
    with open('test.doc', 'w') as f:
        for cptr in chapters:
            f.write(f'\nГлава {cptr.number}\n\n')
            for i in cptr.comments.all():
                f.write(
                    f'{i.name}\n\n'
                    f'Стр.{i.page_number_by_2012} / '
                    f'Стр.{i.page_number_by_2021}\n\n'
                    f'{html.unescape(
                        bleach.clean(i.comment_text, strip=True)
                    )}\n\n'
                )
