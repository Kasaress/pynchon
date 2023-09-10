import re
import datetime as dt
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import (
    Article, Book, Comment, CircleTableCharacters,
    Chapter, TableChronology, TableСharacters
)


def index(request):
    """ Главная страница книги 'Радуга тяготения'. """
    template = 'wiki/index.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'url_name': 'index',
    }
    return render(request, template, context=context)


def about_project(request):
    """ Страница о проекте. """
    template = 'wiki/about-project.html'
    today = dt.date.today()
    planned = Article.objects.filter(attitude='Запланированные мероприятия',
                                     date__gte=today)
    past = Article.objects.filter(attitude='Записи встреч')
    context = {
        'planned': planned,
        'past': past,
    }
    return render(request, template, context)


def contacts(request):
    """ Страница с контактами. """
    template = 'wiki/contacts.html'
    return render(request, template)


def creators(request):
    """ Страница с авторами. """
    template = 'wiki/creators.html'
    articles = Article.objects.filter(attitude='Авторы')
    context = {
        'articles': articles
    }
    return render(request, template, context)


def other_books(request):
    """ Страница с другими книгами. """
    template = 'wiki/other-books.html'
    return render(request, template)


def author(request):
    """ Страница об авторе. """
    template = 'wiki/author.html'
    context = {
    }
    return render(request, template, context=context)


def rainbow_part1(request):
    """ Страница со статьей. """
    template = 'wiki/chapter1.html'
    articles = Article.objects.filter(attitude='Раздел 1')
    context = {
        'articles': articles
    }
    return render(request, template, context=context)


def rainbow_part2(request):
    """ Страница с примечаниями. """
    template = 'wiki/chapter2.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapters = Chapter.objects.filter(book=book)
    context = {
        'book': book,
        'start_chapter': Chapter.objects.filter(book=book).get(number='1.1'),
        'chapters': chapters,
        'search_model': 'comments'
    }
    return render(request, template, context)


def rainbow_part3(request):
    """ Страница с комментариями к главам. """
    template = 'wiki/chapter3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'start_chapter': Chapter.objects.filter(book=book).get(number='1.1'),
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part4(request):
    """ Страница со статьями. """
    template = 'wiki/chapter4.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 4')
    context = {
        'book': book,
        'articles': articles
    }
    return render(request, template, context)


def rainbow_part5(request):
    """ Страница с хронологией. """
    template = 'wiki/chapter5.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'start_event': TableChronology.objects.get(id=172),
        'events': TableChronology.objects.all(),
        'search_model': 'chronology'
    }
    return render(request, template, context)


def rainbow_part6(request):
    """ Страница с персонажами. """
    template = 'wiki/chapter6.html'
    circles = CircleTableCharacters.objects.all()
    context = {
        'circles': circles,
        'search_model': 'characters'
    }
    return render(request, template, context)


def rainbow_part7(request):
    """ Страница со статьей. """
    template = 'wiki/chapter7.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 7')
    context = {
        'book': book,
        'articles': articles
    }
    return render(request, template, context)


def get_comments(request):
    """ Динамический контент комментариев главы. """
    template = 'wiki/comments.html'
    selected_chapter_id = request.GET.get('chapter_id')
    comments = Comment.objects.filter(chapter_id=selected_chapter_id)
    context = {
        'selected_chapter_id': selected_chapter_id,
        'comments': comments,
    }
    return render(request, template, context)


def get_summary(request):
    """ Динамический контент краткого содержания главы. """
    template = 'wiki/summary.html'
    selected_chapter_id = request.GET.get('chapter_id')
    chapter = Chapter.objects.get(pk=selected_chapter_id)
    context = {
        'selected_chapter_id': selected_chapter_id,
        'chapter': chapter,
    }
    return render(request, template, context)


def in_development(request):
    """ Страница в разработке. """
    template = 'wiki/in_development.html'
    return render(request, template)


def search(request):
    """ Результаты поиска. """
    query = request.GET.get('q', '')
    search_model = request.GET.get('chapter')
    results = []
    if search_model == 'comments':
        results = Comment.objects.filter(comment_text__icontains=query)
        for result in results:
            result.comment_text = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.comment_text, flags=re.IGNORECASE
            )
    elif search_model == 'chronology':
        results = TableChronology.objects.filter(
            Q(description__icontains=query) | Q(date__icontains=query)
        )
        for result in results:
            result.description = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.description, flags=re.IGNORECASE
            )
            result.date = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.date, flags=re.IGNORECASE
            )
    elif search_model == 'characters':
        results = TableСharacters.objects.filter(name__icontains=query)
        for result in results:
            result.name = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.name, flags=re.IGNORECASE
            )
    return render(request, 'wiki/search_results.html', {
        'results': results, 'query': query, 'search_model': search_model})
