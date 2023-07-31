import re
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import (
    Article, Book, Comment, CircleTableCharacters, Chapter, TableChronology
)
from .decorators import page_in_development


def index(request):
    """ Главная страница книги радуга тяготения. """
    template = 'wiki/index.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'url_name': 'index',
    }
    return render(request, template, context=context)


def about(request):
    """ Страница описания. """
    template = 'wiki/about.html'
    return render(request, template)


def author(request):
    """ Страница об авторе. """
    template = 'wiki/author.html'
    articles = Article.objects.filter(chapter=777)
    context = {
        'articles': articles
    }
    return render(request, template, context=context)


def rainbow_part1(request):
    template = 'wiki/rainbow_part1.html'
    articles = Article.objects.filter(chapter=1)
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 1: для чего читать радугу',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'url_name': 'rainbow_part1',
        'articles': articles,
        'breadcrumbs': breadcrumbs
    }
    return render(request, template, context=context)


def rainbow_part2(request):
    template = 'wiki/rainbow_part2.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 2: примечания к каждой главе',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part3(request):
    template = 'wiki/rainbow_part3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 3: краткое содержание и комментарии по главам',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part4(request):
    template = 'wiki/rainbow_part4.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 4: статьи с объяснениями',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part5(request):
    template = 'wiki/rainbow_part5.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(chapter=6)
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 5: хронология романа',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'rows': TableChronology.objects.all(),
        'articles': articles,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def rainbow_part6(request):
    template = 'wiki/rainbow_part6.html'
    circles = CircleTableCharacters.objects.all()
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 6: персонажи - таблица и схема',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'circles': circles,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


@page_in_development
def rainbow_part7(request):
    template = 'wiki/rainbow_part7.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 7: объяснение',
            'url_name': reverse('wiki:rainbow_part1')
        }
    ]
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def search(request):
    """ Результаты поиска. """
    query = request.GET.get('q', '')
    results = Comment.objects.filter(comment_text__icontains=query)
    for result in results:
        result.comment_text = re.sub(r'(%s)' % re.escape(query),
                                     r'<span class="highlighted">\1</span>',
                                     result.comment_text, flags=re.IGNORECASE
                                     )
    return render(
        request, 'wiki/search.html', {'results': results, 'query': query}
    )


def rainbow_notes(request, chapter_number):
    """ Страница главы, на которой видно все примечания к главе. """

    template = 'wiki/rainbow_notes.html'
    chapter = get_object_or_404(Chapter, number=chapter_number)
    book = get_object_or_404(Book, name='Радуга тяготения')
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 2: примечания к каждой главе',
            'url_name': reverse('wiki:rainbow_part2')
        },
        {
            'title': f'Примечания к главе {chapter}',
            'url_name': reverse('wiki:rainbow_notes', args={chapter})
        }
    ]
    context = {
        'chapter': chapter,
        'comments': chapter.comments.all(),
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
        'search': search
    }
    return render(request, template, context)


def rainbow_comments(request, chapter_number):
    """ Страница главы, на которой видно все комментарии к главе. """

    template = 'wiki/rainbow_comments.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapter = get_object_or_404(Chapter, number=chapter_number)
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 3: краткое содержание и комментарии по главам',
            'url_name': reverse('wiki:rainbow_part3')},
        {
            'title': f'Комментариии к главе {chapter}',
            'url_name': reverse('wiki:rainbow_comments', args={chapter})
        }
    ]
    context = {
        'book': book,
        'comments': chapter.comments.all(),
        'chapter': chapter,
        'chapters': Chapter.objects.filter(book=book).all(),
        'breadcrumbs': breadcrumbs,
    }
    return render(request, template, context)


def double_katie(request):
    breadcrumbs = [
        {
            'title': 'Главная', 'url_name': reverse('wiki:index')
        },
        {
            'title': 'Раздел 4: статьи с объяснениями',
            'url_name': reverse('wiki:rainbow_part4')
        },
        {
            'title': 'Двойничество Катье',
            'url_name': reverse('wiki:double_katie')
        }
    ]
    return render(request, 'wiki/double_katie.html',
                  context={'breadcrumbs': breadcrumbs})


def in_development(request):
    """ Страница в разработке. """
    template = 'wiki/in_development.html'
    return render(request, template)
