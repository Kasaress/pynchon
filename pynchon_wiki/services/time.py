from django.utils.datetime_safe import datetime


def get_datetime_today() -> str:
    """ Функция возвращает дату сегодняшнего дня. """

    return datetime.today().strftime('%Y-%m-%d')
