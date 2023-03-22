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
