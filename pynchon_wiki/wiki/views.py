from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Book, Chapter, Comment, TableChronology


# Главная страница
@login_required
def index(request):
    template = 'wiki/index.html'
    return render(request, template)

# О проекте
@login_required
def about(request):
    template = 'wiki/about.html'
    return render(request, template)

# Страница книги радуга тяготения
@login_required
def rainbow(request):
    template = 'wiki/rainbow.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part1(request):
    template = 'wiki/rainbow_part1.html'
    return render(request, template)


def rainbow_part2(request):
    template = 'wiki/rainbow_part2.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part3(request):
    template = 'wiki/rainbow_part3.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part4(request):
    template = 'wiki/rainbow_part4.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part5(request):
    template = 'wiki/rainbow_part5.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part6(request):
    template = 'wiki/rainbow_part6.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)


def rainbow_part7(request):
    template = 'wiki/rainbow_part7.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'book': book,
        'chapters': Chapter.objects.filter(book=book).all(),
    }
    return render(request, template, context)

# Страница главы, на которой видно все примечания к главе
def rainbow_notes(request, chapter_number):
    template = 'wiki/rainbow_notes.html'
    chapter = get_object_or_404(Chapter, number=chapter_number)
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'chapter': chapter,
        'comments': chapter.comments.all(),
        'chapters': Chapter.objects.filter(book=book).all()
    }
    return render(request, template, context)


# Страница главы, на которой видно все комментарии к главе
def rainbow_comments(request, chapter_number):
    template = 'wiki/rainbow_comments.html'
    book = get_object_or_404(Book, name='Радуга тяготения')
    chapter = get_object_or_404(Chapter, number=chapter_number)
    context = {
        'book': book,
        'comments': chapter.comments.all(),
        'chapter': chapter,
        'chapters': Chapter.objects.filter(book=book).all()
        }
    return render(request, template, context)


def double_katie(request):
    return render(request, 'wiki/double_katie.html')


def chronology(request):
    return render(
        request,
        'wiki/chronology.html',
        context = {'rows': TableChronology.objects.all()}
    )