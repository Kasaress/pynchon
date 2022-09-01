from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница книги радуга тяготения
def rainbow(request):
    return HttpResponse('Страница Радуги тяготения')


# Страница главы, на которой видно все комментарии к главе
def rainbow_chapter(request, chapter):
    return HttpResponse(f'Глава {chapter} радуги тяготения')
