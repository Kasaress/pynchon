from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('search', views.search, name='search'),
    path('in_development', views.in_development, name='in_development'),
    path('comments/', views.get_comments, name='get_comments'),
    path('summary/', views.get_summary, name='get_summary'),
    path('rainbow_part1', views.rainbow_part1, name='rainbow_part1'),
    path('rainbow_part1/article1', views.article1, name='article1'),
    path('rainbow_part1/article2', views.article2, name='article2'),
    path('rainbow_part2', views.rainbow_part2, name='rainbow_part2'),
    path('rainbow_part3', views.rainbow_part3, name='rainbow_part3'),
    path('rainbow_part4', views.rainbow_part4, name='rainbow_part4'),
    path('rainbow_part5', views.rainbow_part5, name='rainbow_part5'),
    path('rainbow_part6', views.rainbow_part6, name='rainbow_part6'),
    path(
        'rainbow_part6_map', views.rainbow_part6_map, name='rainbow_part6_map'
    ),
    path('rainbow_part7', views.rainbow_part7, name='rainbow_part7'),
    path('author', views.author, name='author'),
    path('about-project', views.about_project, name='about-project'),
    path('other-books', views.other_books, name="other-books"),
    path('contacts', views.contacts, name='contacts'),
    path('creators', views.creators, name='creators'),
    path('', views.index, name='index'),
]
