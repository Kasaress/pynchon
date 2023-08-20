import re
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import (
    Article, Book, Comment, CircleTableCharacters,
    Chapter, TableChronology, TableСharacters
)


def download_chronology(request):
    """ Загрузка списка хронологии. """
    chronology = TableChronology.objects.all()
    content = "Дата\tСобытие\n"
    for event in chronology:
        content += f"{event.date}\t{event.description}\n"

    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="chronology.txt"'

    return response


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


def about_project(request):
    """ Страница о проекте. """
    template = 'wiki/about-project.html'
    articles = Article.objects.filter(chapter=222)
    context = {
        'articles': articles
    }
    return render(request, template, context)


def contacts(request):
    """ Страница с контактами. """
    template = 'wiki/contacts.html'
    return render(request, template)


def creators(request):
    """ Страница с авторами. """
    template = 'wiki/creators.html'
    return render(request, template)


def other_books(request):
    """ Страница с другими книгами. """
    template = 'wiki/other-books.html'
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
    template = 'wiki/chapter1.html'
    articles = Article.objects.filter(chapter=1)
    context = {
        'url_name': 'rainbow_part1',
        'articles': articles,
    }
    return render(request, template, context=context)


def rainbow_part2(request):
    template = 'wiki/chapter2.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'search_model': 'comments'
    }
    return render(request, template, context)


def rainbow_part3(request):
    template = 'wiki/chapter3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part4(request):
    template = 'wiki/chapter4.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(chapter=4)
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'articles': articles
    }
    return render(request, template, context)


def rainbow_part5(request):
    template = 'wiki/chapter5.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(chapter=6)
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'rows': TableChronology.objects.all(),
        'articles': articles,
        'search_model': 'chronology'
    }
    return render(request, template, context)


def rainbow_part6(request):
    template = 'wiki/chapter6.html'
    circles = CircleTableCharacters.objects.all()
    context = {
        'circles': circles,
        'search_model': 'characters'
    }
    return render(request, template, context)


def rainbow_part7(request):
    template = 'wiki/chapter7.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
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
