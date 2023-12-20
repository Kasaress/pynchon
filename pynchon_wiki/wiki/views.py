import re
import datetime as dt
from django.db.models import Q
from django.core.mail.message import EmailMessage
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import get_object_or_404, render

from pynchon_wiki.settings import (
    EMAIL_HOST_USER, EMAIL_RECIPIENT, RAINBOW_START_EVENT, V_START_EVENT,
    RAINBOW_BOOK, V_BOOK
)
from .decorators import page_in_development
from .forms import ContactForm
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
    articles = Article.objects.filter(attitude='О сайте')
    planned = Article.objects.filter(
        attitude='Запланированные мероприятия',
        date__gte=today
    )
    past = Article.objects.filter(attitude='Записи встреч')
    context = {
        'planned': planned,
        'past': past,
        'articles': articles
    }
    return render(request, template, context)


def contacts(request):
    """ Страница для отправки контактной формы. """
    template = 'wiki/contacts.html'
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "pynchon.ru"
            body = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
                'file': form.cleaned_data['file'],
                'captcha': form.cleaned_data['captcha']
            }
            msg = (
                f'Новое сообщение от пользователя: {body["username"]}\n'
                f'Email: {body["email"]}\n'
                f'Текст сообщения: {body["message"]}'
            )
            email = EmailMessage(
                subject, msg, EMAIL_HOST_USER, [EMAIL_RECIPIENT]
            )
            if body['file']:
                attachment_file = body['file']
                email.attach(attachment_file.name, attachment_file.read())
            try:
                email.send()
            except BadHeaderError:
                return HttpResponse('Найден неккоректный заголовок')
            return render(request, template_name='wiki/message_sent.html')

    form = ContactForm()
    return render(request, template, {'form': form})


def creators(request):
    """ Страница с авторами. """
    template = 'wiki/creators.html'
    articles = Article.objects.filter(attitude='Авторы')
    context = {
        'articles': articles
    }
    return render(request, template, context)


@page_in_development
def other_books(request):
    """ Страница с другими книгами. """
    template = 'wiki/other-books.html'
    return render(request, template)


def author(request):
    """ Страница об авторе. """
    template = 'wiki/author.html'
    articles = Article.objects.filter(attitude='Томас Пинчон')
    context = {
        'articles': articles
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


def article1(request):
    """ Страница со статьей. """
    template = 'wiki/article1.html'
    articles = Article.objects.filter(attitude='Раздел 1 (статья 1)')
    context = {
        'articles': articles
    }
    return render(request, template, context=context)


def article2(request):
    """ Страница со статьей. """
    template = 'wiki/article2.html'
    articles = Article.objects.filter(attitude='Раздел 1 (статья 2)')
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
        'chapters': chapters,
        'search_model': 'comments'
    }
    return render(request, template, context)


def rainbow_part2_detail(request, comment_id):
    """ Страница с отдельным примечанием. """
    template = 'wiki/chapter2_detail.html'
    comment = Comment.objects.get(pk=comment_id)
    context = {
        'comment': comment
    }
    return render(request, template, context)


def rainbow_part3(request):
    """ Страница с комментариями к главам. """
    template = 'wiki/chapter3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
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
    articles = Article.objects.filter(attitude='Раздел 5')
    context = {
        'start_event': TableChronology.objects.get(id=RAINBOW_START_EVENT),
        'articles': articles,
        'events': TableChronology.objects.filter(book=RAINBOW_BOOK),
        'search_model': 'chronology'
    }
    return render(request, template, context)


def rainbow_part6(request):
    """ Страница с персонажами. """
    template = 'wiki/chapter6.html'
    circles = CircleTableCharacters.objects.filter(book=RAINBOW_BOOK)
    context = {
        'circles': circles,
        'search_model': 'characters'
    }
    return render(request, template, context)


def rainbow_part6_map(request):
    """ Страница с картой перемещений персонажей. """
    template = 'wiki/chapter6_map.html'
    context = {
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


def search(request):
    """ Результаты поиска. """
    query = request.GET.get('q', '')
    search_model = request.GET.get('chapter')
    results = []
    if search_model == 'comments':
        results = Comment.objects.filter(
            Q(comment_text__icontains=query) | Q(name__icontains=query))
        for result in results:
            result.comment_text = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.comment_text, flags=re.IGNORECASE
            )
            result.name = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.name, flags=re.IGNORECASE
            )
    elif search_model == 'v_comments':
        results = Comment.objects.filter(
            Q(comment_text__icontains=query) | Q(name__icontains=query))
        for result in results:
            result.comment_text = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.comment_text, flags=re.IGNORECASE
            )
            result.name = re.sub(
                r'(%s)' % re.escape(query),
                r'<span class="highlighted">\1</span>',
                result.name, flags=re.IGNORECASE
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


def v_part1(request):
    """ Страница со статьей. """
    template = 'wiki/v_chapter1.html'
    articles = Article.objects.filter(attitude='V Раздел 1')
    context = {
        'articles': articles
    }
    return render(request, template, context=context)


def v_article1(request):
    """ Страница со статьей. """
    template = 'wiki/v_article1.html'
    articles = Article.objects.filter(attitude='V Раздел 1 (статья 1)')
    context = {
        'articles': articles
    }
    return render(request, template, context=context)


def v_article2(request):
    """ Страница со статьей. """
    template = 'wiki/v_article2.html'
    articles = Article.objects.filter(attitude='V Раздел 1 (статья 2)')
    context = {
        'articles': articles
    }
    return render(request, template, context=context)


def v_part2(request):
    """ Страница с примечаниями. """
    template = 'wiki/v_chapter2.html'
    book = get_object_or_404(Book, name='V')
    chapters = Chapter.objects.filter(book=book).order_by('sort')
    context = {
        'book': book,
        'chapters': chapters,
        'search_model': 'v_comments'
    }
    return render(request, template, context)


def v_get_comments(request):
    """ Динамический контент комментариев главы. """
    template = 'wiki/v_comments.html'
    selected_chapter_id = request.GET.get('chapter_id')
    comments = Comment.objects.filter(chapter_id=selected_chapter_id)
    context = {
        'selected_chapter_id': selected_chapter_id,
        'comments': comments,
    }
    return render(request, template, context)


def v_part2_detail(request, comment_id):
    """ Страница с отдельным примечанием. """
    template = 'wiki/v_chapter2_detail.html'
    comment = Comment.objects.get(pk=comment_id)
    context = {
        'comment': comment
    }
    return render(request, template, context)


def v_part3(request):
    """ Страница со статьями. """
    template = 'wiki/v_chapter3.html'
    book = get_object_or_404(Book, name='V')
    articles = Article.objects.filter(attitude='V Раздел 3')
    context = {
        'book': book,
        'articles': articles
    }
    return render(request, template, context)


def v_part4(request):
    """ Страница с хронологией. """
    template = 'wiki/v_chapter4.html'
    book = get_object_or_404(Book, name='V')
    articles = Article.objects.filter(attitude='V Раздел 4')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'start_event': TableChronology.objects.get(id=V_START_EVENT),
        'articles': articles,
        'events': TableChronology.objects.filter(book=V_BOOK),
        'search_model': 'chronology'
    }
    return render(request, template, context)


def v_part5(request):
    """ Страница с персонажами. """
    template = 'wiki/v_chapter5.html'
    circles = CircleTableCharacters.objects.filter(book=V_BOOK)
    context = {
        'circles': circles,
        'search_model': 'characters'
    }
    return render(request, template, context)


def v_part5_map(request):
    """ Страница с картой перемещений персонажей. """
    template = 'wiki/v_chapter5_map.html'
    context = {
        'search_model': 'characters'
    }
    return render(request, template, context)


def in_development(request):
    """ Страница в разработке. """
    template = 'includes/in_development.html'
    return render(request, template)
