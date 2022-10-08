from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import ImageField, get_thumbnail

User = get_user_model()


class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(
        verbose_name='Описание книги'
    )
    
    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'

    def __str__(self) -> str:
        return str(self.name)


class Chapter(models.Model):
    number = models.CharField(max_length=5)
    book = models.ForeignKey(
        Book,
        related_name='chapters',
        verbose_name='Книга',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name_plural = 'Главы'
        verbose_name = 'Глава'
        
    def __str__(self) -> str:
        return str(self.number)

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
        #upload_to='comments/'
    )
    book = models.ForeignKey(
        Book,
        related_name='comments',
        verbose_name='Книга',
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
    page_number_by_2012 = models.IntegerField()
    page_number_by_2021 = models.IntegerField()
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
        ordering = ('order_number',)
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'

    def get_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="max-height: 500px;">')
        else:
            return 'нет картинки'