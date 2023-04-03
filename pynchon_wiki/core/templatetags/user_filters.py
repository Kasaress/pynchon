from django import template

from core.models import TopMenu

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def sort_chapters(chapters):
    def chapter_key(chapter):
        return tuple(int(part) for part in chapter.number.split('.'))

    return sorted(chapters, key=chapter_key)


@register.simple_tag
def show_top_menu():
    menu = TopMenu.objects.filter(is_active=True,
                                  deleted_at__isnull=True
                                  ).order_by('sort')
    return menu
