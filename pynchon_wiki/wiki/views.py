from django.shortcuts import get_object_or_404, render

from .models import Book, Chapter, Comment, TableChronology


# Главная страница
def index(request):
    template = 'wiki/index.html'
    return render(request, template)

# О проекте
def about(request):
    template = 'wiki/about.html'
    return render(request, template)

# Страница книги радуга тяготения
def rainbow(request):
    template = 'wiki/rainbow.html'
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
    return render(request, 'wiki/chronology.html', context = {'rows': TableChronology.objects.all()})