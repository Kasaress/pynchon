from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """ Базовая модель. """

    created_at = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Активен',
        default=True,
        null=False,
        blank=False
    )
    deleted_at = models.DateTimeField(
        'Дата удаления',
        default=None,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class BaseNameModel(BaseModel):
    """ Базовая модель с названием. """

    name = models.CharField(
        'Название',
        max_length=settings.DEFAULT_NAME_LENGTH
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class TopMenu(BaseNameModel):
    """ Модель верхнеуровневого меню. """

    url = models.CharField(
        'Ссылка на страницу',
        max_length=settings.DEFAULT_NAME_LENGTH,
        blank=True,
        null=True
    )
    auth_only = models.BooleanField(
        'Только для авторизованных',
        default=False
    )
    sort = models.PositiveSmallIntegerField(
        'Сортировка',
        default=100
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        db_table = 'menus'
