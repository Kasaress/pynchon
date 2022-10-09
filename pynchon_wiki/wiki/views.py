from django.shortcuts import get_object_or_404, render

from .models import Book, Chapter, Comment


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


# Страница главы, на которой видно все комментарии к главе
def rainbow_chapter(request, chapter_number):
    template = 'wiki/chapter.html'
    chapter = get_object_or_404(Chapter, number=chapter_number)
    book = get_object_or_404(Book, name='Радуга тяготения')
    context = {
        'chapter': chapter,
        'comments': chapter.comments.all(),
        'chapters': Chapter.objects.filter(book=book).all()
    }
    return render(request, template, context)
