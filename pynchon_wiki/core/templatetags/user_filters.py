import os.path
from typing import Optional

from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def sort_chapters(chapters):
    def chapter_key(chapter):
        return tuple(int(part) for part in chapter.number.split('.'))

    return sorted(chapters, key=chapter_key)


@register.filter
def tstamp(file) -> Optional[str]:
    from django.contrib.staticfiles import finders
    result = finders.find(file)
    if result:
        file_time = int(os.path.getctime(result))
        return f'{file}?={file_time}'
    return
