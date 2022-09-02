from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        verbose_name='Описание книги'
    )


class Chapter(models.Model):
    number = models.IntegerField()
    book = models.ForeignKey(
        Book,
        related_name='chapters',
        verbose_name='Книга',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class Comment(models.Model):
    origin_text = models.CharField(
        max_length=200,
        verbose_name='Оригинальный текст книги'
    )
    comment_text = models.TextField(
        verbose_name='Текст комментария'
    )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Картинка',
        # upload_to='wiki/'
    )
    book = models.ForeignKey(
        Book,
        related_name='comments',
        verbose_name='Номер главы',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    chapter = models.ForeignKey(
        Chapter,
        related_name='comments',
        verbose_name='Номер главы',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    page_number = models.IntegerField()
    order_number = models.IntegerField()
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Опубликовано'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор')

    class Meta:
        ordering = ('-order_number',)
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'


