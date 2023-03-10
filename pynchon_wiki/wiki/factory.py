from factory import Faker, Iterator, django, SubFactory

from users.models import User
from wiki.models import (Book, TableChronology, Comment, Chapter, ChapterLink,
                         CommentLink)


class BookFactory(django.DjangoModelFactory):
    class Meta:
        model = Book

    name = Faker('word')
    description = Faker('paragraph')


class ChapterFactory(django.DjangoModelFactory):
    class Meta:
        model = Chapter

    number = Faker('pyint')
    book = Iterator(Book.objects.all())
    description = Faker('paragraph')
    book_part = Faker('pyint')
    summary = Faker('paragraph')
    interpretation = Faker('paragraph')
    image = Faker('file_path', category='image', extension='jpg')


class ChapterLinkFactory(django.DjangoModelFactory):
    class Meta:
        model = ChapterLink

    link = Faker('url')
    chapter = SubFactory(ChapterFactory)


class CommentFactory(django.DjangoModelFactory):
    class Meta:
        model = Comment

    name = Faker('word')
    comment_text = Faker('paragraph')
    image = Faker('file_path', category='image', extension='jpg')
    book = Iterator(Book.objects.all())
    chapter = Iterator(Chapter.objects.all())
    page_number_by_2012 = Faker('pyint')
    page_number_by_2021 = Faker('pyint')
    sort = Faker('pyint')
    author = Iterator(User.objects.all())


class CommentLinkFactory(django.DjangoModelFactory):
    class Meta:
        model = CommentLink

    link = Faker('url')
    comment = SubFactory(CommentFactory)


class TableChronologyFactory(django.DjangoModelFactory):
    class Meta:
        model = TableChronology

    date = Faker('date')
    description = Faker('paragraph')
    sort = Faker('pyint')
