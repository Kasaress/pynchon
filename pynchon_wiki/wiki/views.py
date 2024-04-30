from itertools import chain
import datetime as dt
from django.core.mail.message import EmailMessage
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    return render(request, template, context)


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
    return render(request, template, context)


def rainbow_part1(request):
    """ Страница со статьей. """
    template = 'wiki/chapter1.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 1')
    context = {
        'book': book,
        'articles': articles,
        'search_model': 'articles_1'
    }
    return render(request, template, context)


def article1(request):
    """ Страница со статьей. """
    template = 'wiki/article1.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 1 (статья 1)')
    context = {
        'book': book,
        'articles': articles,
        'search_model': 'articles_1'
    }
    return render(request, template, context)


def article2(request):
    """ Страница со статьей. """
    template = 'wiki/article2.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 1 (статья 2)')
    context = {
        'book': book,
        'articles': articles,
        'search_model': 'articles_1'
    }
    return render(request, template, context)


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
    book = get_object_or_404(Book, name='Радуга тяготения')
    comment = Comment.objects.get(pk=comment_id)
    context = {
        'book': book,
        'comment': comment,
        'search_model': 'comments'
    }
    return render(request, template, context)


def rainbow_part3(request):
    """ Страница с комментариями к главам. """
    template = 'wiki/chapter3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
        'search_model': 'chapters'
    }
    return render(request, template, context)


def rainbow_part3_detail(request, chapter_id):
    """ Страница с отдельным комментарием. """
    template = 'wiki/chapter3_detail.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapter = Chapter.objects.get(pk=chapter_id)
    context = {
        'book': book,
        'chapter': chapter,
        'search_model': 'chapters'
    }
    return render(request, template, context)


def rainbow_part4(request):
    """ Страница со статьями. """
    template = 'wiki/chapter4.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 4')
    context = {
        'book': book,
        'articles': articles,
        'search_model': 'articles_4'
    }
    return render(request, template, context)


def rainbow_part4_detail(request, article_id):
    """ Страница с отдельной статьей. """
    template = 'wiki/chapter4_detail.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    article = Article.objects.get(pk=article_id)
    context = {
        'book': book,
        'article': article,
        'search_model': 'articles_4'
    }
    return render(request, template, context)


def rainbow_part5(request):
    """ Страница с хронологией. """
    template = 'wiki/chapter5.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    articles = Article.objects.filter(attitude='Раздел 5')
    context = {
        'book': book,
        'start_event': TableChronology.objects.get(id=RAINBOW_START_EVENT),
        'articles': articles,
        'events': TableChronology.objects.filter(book=RAINBOW_BOOK),
        'search_model': 'chronology'
    }
    return render(request, template, context)


def rainbow_part6(request):
    """ Страница с персонажами. """
    template = 'wiki/chapter6.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    circles = CircleTableCharacters.objects.filter(book=RAINBOW_BOOK)
    context = {
        'book': book,
        'circles': circles,
        'search_model': 'characters'
    }
    return render(request, template, context)


def rainbow_part6_map(request):
    """ Страница с картой перемещений персонажей. """
    template = 'wiki/chapter6_map.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
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
        'articles': articles,
        'search_model': 'articles_7'
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


def search(request, book_id, search_model):
    template = 'wiki/search_results.html'
    q = request.GET.get('q')
    book = get_object_or_404(Book, pk=book_id)
    query_sets = []
    query_sets.extend([
        Comment.objects.search(query=q, book_id=book_id),
        Chapter.objects.search(query=q, book_id=book_id),
        sorted(
            Article.objects.search(query=q, book_id=book_id),
            key=lambda x: x.attitude
        ),
        TableChronology.objects.search(query=q, book_id=book_id),
        TableСharacters.objects.search(query=q, book_id=book_id)
    ])
    final_set = list(chain(*query_sets))
    comments_set = [
        el for el in final_set if el.__class__.__name__ == 'Comment'
    ]
    chapters_set = [
        el for el in final_set if el.__class__.__name__ == 'Chapter'
    ]
    articles_1_set = [
        el for el in final_set
        if el.__class__.__name__ == 'Article'
        and (
            el.attitude == 'Раздел 1' or el.attitude == 'Раздел 1 (статья 1)'
            or el.attitude == 'Раздел 1 (статья 2)'
            or el.attitude == 'V Раздел 1'
        )
    ]
    articles_4_set = [
        el for el in final_set
        if el.__class__.__name__ == 'Article'
        and (el.attitude == 'Раздел 4' or el.attitude == 'V Раздел 3')
    ]
    articles_7_set = [
        el for el in final_set
        if el.__class__.__name__ == 'Article' and el.attitude == 'Раздел 7'
    ]
    chronology_set = [
        el for el in final_set if el.__class__.__name__ == 'TableChronology'
    ]
    characters_set = [
        el for el in final_set if el.__class__.__name__ == 'TableСharacters'
    ]
    context = {
        'q': q,
        'book': book,
        'final_set': final_set,
        'comments_set': comments_set,
        'chapters_set': chapters_set,
        'articles_1_set': articles_1_set,
        'articles_4_set': articles_4_set,
        'articles_7_set': articles_7_set,
        'chronology_set': chronology_set,
        'characters_set': characters_set,
        'search_model': search_model
    }
    return render(request, template, context)


def search_list(request, book_id, search_model):
    template = 'wiki/search_list.html'
    q = request.GET.get('q')
    content = request.GET.get('content')
    book = get_object_or_404(Book, pk=book_id)
    content_list = []
    if content == 'comments':
        content_list.append(Comment.objects.search(query=q, book_id=book_id))
    elif content == 'chapters':
        content_list.append(Chapter.objects.search(query=q, book_id=book_id))
    elif content == 'articles':
        content_list.append(sorted(Article.objects.search(
            query=q, book_id=book_id
        ), key=lambda x: x.attitude))
    elif content == 'chronology':
        content_list.append(TableChronology.objects.search(
            query=q, book_id=book_id
        ))
    elif content == 'characters':
        content_list.append(TableСharacters.objects.search(
            query=q, book_id=book_id
        ))
    content_list = list(chain(*content_list))
    context = {
        'q': q,
        'book': book,
        'content_list': content_list,
        'search_model': search_model
    }
    context['last_question'] = '?q=%s' % q
    current_page = Paginator(content_list, 10)
    page = request.GET.get('page')
    try:
        context['object_list'] = current_page.page(page)
    except PageNotAnInteger:
        context['object_list'] = current_page.page(1)
    except EmptyPage:
        context['object_list'] = current_page.page(current_page.num_pages)
    return render(request, template, context)


def v_index(request):
    """ Главная страница книги 'V.'. """
    template = 'wiki/v_index.html'
    book = get_object_or_404(Book, name='V')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def v_part1(request):
    """ Страница со статьей. """
    template = 'wiki/v_chapter1.html'
    book = get_object_or_404(Book, name='V')
    articles = Article.objects.filter(attitude='V Раздел 1')
    context = {
        'book': book,
        'articles': articles,
        'search_model': 'articles_1'
    }
    return render(request, template, context)


def v_part2(request):
    """ Страница с примечаниями. """
    template = 'wiki/v_chapter2.html'
    book = get_object_or_404(Book, name='V')
    chapters = Chapter.objects.filter(book=book).order_by('sort')
    context = {
        'book': book,
        'chapters': chapters,
        'search_model': 'comments'
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
    book = get_object_or_404(Book, name='V')
    comment = Comment.objects.get(pk=comment_id)
    context = {
        'book': book,
        'comment': comment,
        'search_model': 'comments'
    }
    return render(request, template, context)


def v_part3(request):
    """ Страница со статьями. """
    template = 'wiki/v_chapter3.html'
    book = get_object_or_404(Book, name='V')
    articles = Article.objects.filter(attitude='V Раздел 3')
    context = {
        'book': book,
        'articles': articles,
        'search_model': 'articles_4'
    }
    return render(request, template, context)


def v_part3_detail(request, article_id):
    """ Страница с отдельной статьей. """
    template = 'wiki/v_chapter3_detail.html'
    book = get_object_or_404(Book, name='V')
    article = Article.objects.get(pk=article_id)
    context = {
        'book': book,
        'article': article,
        'search_model': 'articles_4'
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
    book = get_object_or_404(Book, name='V')
    circles = CircleTableCharacters.objects.filter(book=V_BOOK)
    context = {
        'book': book,
        'circles': circles,
        'search_model': 'characters'
    }
    return render(request, template, context)


def v_part5_map(request):
    """ Страница с картой перемещений персонажей. """
    template = 'wiki/v_chapter5_map.html'
    book = get_object_or_404(Book, name='V')
    context = {
        'book': book,
        'search_model': 'characters'
    }
    return render(request, template, context)


def in_development(request):
    """ Страница в разработке. """
    template = 'includes/in_development.html'
    return render(request, template)
