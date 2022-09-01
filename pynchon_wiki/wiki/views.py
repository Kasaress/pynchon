from django.http import HttpResponse
from django.shortcuts import render



# Главная страница
def index(request):
    template = 'wiki/index.html'
    return render(request, template)


# Страница книги радуга тяготения
def rainbow(request):
    template = 'wiki/rainbow.html'
    return render(request, template)


# Страница главы, на которой видно все комментарии к главе
def rainbow_chapter(request, chapter):
    template = 'wiki/chapter.html'
    context = {
        'chapter': chapter
    }
    return render(request, template, context)
