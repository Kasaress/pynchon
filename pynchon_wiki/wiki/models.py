from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Q
from django.template.defaultfilters import truncatechars
from ckeditor.fields import RichTextField

from core.models import BaseModel, BaseNameModel

User = get_user_model()

CHOICES_CHAPTER = [
    ('Другое', 'Другое'), ('Раздел 1', 'Раздел 1'),
    ('V Раздел 1', 'V Раздел 1'), ('Раздел 4', 'Раздел 4'),
    ('V Раздел 4', 'V Раздел 4'), ('V Раздел 5', 'V Раздел 5'),
    ('Раздел 1 (статья 1)', 'Раздел 1 (статья 1)'),
    ('V Раздел 3', 'V Раздел 3'),
    ('Раздел 1 (статья 2)', 'Раздел 1 (статья 2)'),
    ('Раздел 5', 'Раздел 5'), ('Раздел 7', 'Раздел 7'),
    ('Авторы', 'Авторы'), ('Томас Пинчон', 'Томас Пинчон'),
    ('Запланированные мероприятия', 'Запланированные мероприятия'),
    ('Записи встреч', 'Записи встреч'), ('Другие книги', 'Другие книги'),
    ('О сайте', 'О сайте'), ('Новости', 'Новости')
]


class Book(BaseNameModel):
    """ Модель книг. """

    description = models.TextField(
        verbose_name='Описание книги'
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        db_table = 'books'

    def __str__(self) -> str:
        return self.name


class ChapterManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None, book_id=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (
                Q(pov__icontains=query) | Q(summary__icontains=query)
                | Q(interpretation__icontains=query)
            )
            qs = qs.filter(or_lookup, book_id=book_id)

        return qs


class Chapter(BaseModel):
    """ Модель глав у книг. """
    objects = ChapterManager()

    number = models.CharField(
        verbose_name='Номер главы',
        max_length=8
    )
    book = models.ForeignKey(
        Book,
        verbose_name='Книга',
        related_name='chapters',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = RichTextField(
        verbose_name='Описание главы',
        blank=True,
        null=True
    )
    pov = RichTextField(
        verbose_name='POV',
        blank=True,
        null=True
    )
    book_part = models.PositiveIntegerField(
        verbose_name='Часть книги',
        blank=True, null=True,
        validators=[
            MaxValueValidator(10000)
        ],
    )
    summary = RichTextField(
        verbose_name='Краткое содержание главы',
        blank=True,
        null=True
    )
    interpretation = RichTextField(
        verbose_name='Интерпретация',
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name='Картинка',
        blank=True,
        null=True,
        upload_to='chapters/'
    )
    pages = models.CharField(
        'Номер страниц',
        max_length=50,
        null=True,
        blank=True
    )
    sort = models.IntegerField(
        verbose_name='Сортировка',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
        ordering = ('sort',)
        db_table = 'chapters'

    def __str__(self) -> str:
        return str(self.number)


class ChapterLink(BaseModel):
    """ Модель ссылок для глав книг. """

    link = models.URLField(
        verbose_name='Ссылка к главе',
        blank=True,
        null=True,
    )
    chapter = models.ForeignKey(
        Chapter,
        verbose_name='Глава',
        related_name='chapters',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Ссылка к главе'
        verbose_name_plural = 'Ссылки к главе'
        db_table = 'chapter_links'

    def __str__(self):
        return self.link


class CommentManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None, book_id=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (
                Q(comment_text__icontains=query) | Q(name__icontains=query)
            )
            qs = qs.filter(or_lookup, book_id=book_id)

        return qs


class Comment(BaseNameModel):
    """ Модель комментариев. """
    objects = CommentManager()

    comment_link = models.IntegerField(
        'Cвязь с другим примечанием',
        blank=True,
        null=True
    )
    comment_text = RichTextField(
        'Текст примечания'
    )
    image = models.ImageField(
        verbose_name='Картинка',
        blank=True,
        null=True,
        upload_to='comments/'
    )
    book = models.ForeignKey(
        Book,
        verbose_name='Книга',
        related_name='comments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    chapter = models.ForeignKey(
        Chapter,
        verbose_name='Номер главы',
        related_name='comments',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    page_number_by_2012 = models.PositiveIntegerField(
        verbose_name='Нумерация глав в старом издании',
        blank=True,
        null=True
    )
    page_number_by_2021 = models.PositiveIntegerField(
        verbose_name='Нумерация глав в новом издании',
        blank=True,
        null=True
    )
    sort = models.PositiveBigIntegerField(
        verbose_name='Сортировка',
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ('page_number_by_2012', 'sort')
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'

    @property
    def short_text(self):
        return truncatechars(self.comment_text, 100)

    def __str__(self) -> str:
        return self.name


class CommentLink(BaseModel):
    """ Модель ссылок для комментариев. """

    link = models.URLField(
        verbose_name='Ссылка к комментарию',
        blank=True,
        null=True,
    )
    comment = models.ForeignKey(
        Comment,
        verbose_name='Комментарий',
        related_name='comments',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Ссылка к примечанию'
        verbose_name_plural = 'Ссылки к примечанию'
        db_table = 'comment_links'

    def __str__(self) -> str:
        return self.link


class TableChronologyManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None, book_id=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (
                Q(date__icontains=query) | Q(description__icontains=query)
            )
            qs = qs.filter(or_lookup, book_id=book_id)

        return qs


class TableChronology(BaseModel):
    """ Модель таблицы для определения хронологии. """
    objects = TableChronologyManager()

    date = models.CharField(
        max_length=50,
        verbose_name='Дата',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Событие',
        blank=True,
        null=True
    )
    sort = models.CharField(
        max_length=10,
        verbose_name='Сортировка',
        blank=True,
        null=True
    )
    event_type = models.PositiveSmallIntegerField(
        'Тип события',
        blank=True,
        null=True
    )
    book = models.ForeignKey(
        Book,
        verbose_name='Книга',
        related_name='chronology',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Строка таблицы хронологии'
        verbose_name_plural = 'Строки таблицы хронологии'
        db_table = 'chronologies'
        ordering = ('sort',)

    def __str__(self) -> str:
        return self.description


class ArticleManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None, book_id=None, attitude=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (Q(name__icontains=query) | Q(text__icontains=query))
            qs = qs.filter(or_lookup, book_id=book_id)
            if attitude:
                if attitude in [
                    'Раздел 1', 'Раздел 1 (статья 1)',
                    'Раздел 1 (статья 2)', 'V Раздел 1'
                ]:
                    qs = qs.filter(
                        or_lookup, book_id=book_id, attitude__in=[
                            'Раздел 1', 'V Раздел 1', 'Раздел 1 (статья 1)',
                            'Раздел 1 (статья 2)',
                        ]
                    )
                elif attitude in ['Раздел 4', 'V Раздел 3']:
                    qs = qs.filter(
                        or_lookup, book_id=book_id, attitude__in=[
                            'Раздел 4', 'V Раздел 3'
                        ]
                    )
                elif attitude == 'Раздел 7':
                    qs = qs.filter(
                        or_lookup, book_id=book_id, attitude='Раздел 7'
                    )
        return qs


class Article(BaseNameModel):
    """ Модель статей. """
    objects = ArticleManager()

    name = models.CharField(
        'Название',
        max_length=255,
        blank=True,
        null=True
    )
    text = RichTextField(
        'Текст статьи'
    )
    author_article = models.CharField(
        'Автор статьи',
        max_length=50,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор статьи',
        related_name='articles',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Картинка',
        blank=True,
        null=True,
        upload_to='articles/'
    )
    date = models.DateField(
        'Дата',
        blank=True,
        null=True
    )
    sort = models.PositiveSmallIntegerField(
        'Сортировка',
        blank=True,
        null=True
    )
    attitude = models.TextField(
        'Отношение к разделу',
        choices=CHOICES_CHAPTER
    )
    create_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    link = models.URLField(
        verbose_name='Ссылка к статье',
        blank=True,
        null=True
    )
    book_id = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Книга',
        related_name='articles'
    )

    class Meta:
        ordering = ['sort']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        db_table = 'articles'

    def __str__(self):
        return self.text


class CircleTableCharacters(BaseNameModel):
    """ Модель круга в таблице персонажей."""

    book = models.ForeignKey(
        Book,
        verbose_name='Книга',
        related_name='circles',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Круг в таблице персонажей'
        verbose_name_plural = 'Круги в таблице персонажей'
        db_table = 'circles'


class TableСharactersManager(models.Manager):
    use_for_related_fields = True

    def search(self, query=None, book_id=None):
        qs = self.get_queryset()
        if query:
            or_lookup = (
                Q(name__icontains=query) | Q(value_name__icontains=query)
                | Q(characteristics__icontains=query)
                | Q(portrait__icontains=query)
                | Q(circle__name__icontains=query)
            )
            qs = qs.filter(or_lookup, book_id=book_id)

        return qs


class TableСharacters(BaseNameModel):
    """ Модель таблицы персонажей."""
    objects = TableСharactersManager()

    value_name = models.TextField(
        'Имя в оригинале и значение',
        null=True,
        blank=True
    )
    characteristics = models.TextField(
        'Характеристика',
        null=True,
        blank=True
    )
    portrait = models.TextField(
        'Портрет',
        null=True,
        blank=True
    )
    groups = models.TextField(
        'Группы',
        null=True,
        blank=True
    )
    mentions = models.TextField(
        'Упоминания'
    )
    circle = models.ForeignKey(
        CircleTableCharacters,
        on_delete=models.CASCADE,
        verbose_name='Круг персонажа',
        related_name='characters'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name='Книга',
        related_name='characters'
    )

    class Meta:
        ordering = ['pk']
        verbose_name = 'Запись в таблице персонажей'
        verbose_name_plural = 'Записи в таблице персонажей'
        db_table = 'characters'

    def __str__(self):
        return self.name
