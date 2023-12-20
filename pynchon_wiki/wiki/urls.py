from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('rainbow_part1', views.rainbow_part1, name='rainbow_part1'),
    path('rainbow_part1/article1', views.article1, name='article1'),
    path('rainbow_part1/article2', views.article2, name='article2'),
    path('rainbow_part2', views.rainbow_part2, name='rainbow_part2'),
    path(
        'rainbow_part2_detail/<int:comment_id>', views.rainbow_part2_detail,
        name='rainbow_part2_detail'
    ),
    path('rainbow_part3', views.rainbow_part3, name='rainbow_part3'),
    path('rainbow_part4', views.rainbow_part4, name='rainbow_part4'),
    path('rainbow_part5', views.rainbow_part5, name='rainbow_part5'),
    path('rainbow_part6', views.rainbow_part6, name='rainbow_part6'),
    path(
        'rainbow_part6_map', views.rainbow_part6_map, name='rainbow_part6_map'
    ),
    path('rainbow_part7', views.rainbow_part7, name='rainbow_part7'),
    path('v_part1', views.v_part1, name='v_part1'),
    path('v/article1', views.v_article1, name='v_article1'),
    path('v/article2', views.v_article2, name='v_article2'),
    path('v_part2', views.v_part2, name='v_part2'),
    path('v_comments/', views.v_get_comments, name='v_get_comments'),
    path(
        'v_part2_detail/<int:comment_id>', views.v_part2_detail,
        name='v_part2_detail'
    ),
    path('v_part3', views.v_part3, name='v_part3'),
    path('v_part4', views.v_part4, name='v_part4'),
    path('v_part5', views.v_part5, name='v_part5'),
    path('v_part5_map', views.v_part5_map, name='v_part5_map'),
    path('in_development', views.in_development, name='in_development'),
    path('about-project', views.about_project, name='about-project'),
    path('other-books', views.other_books, name="other-books"),
    path('comments/', views.get_comments, name='get_comments'),
    path('summary/', views.get_summary, name='get_summary'),
    path('contacts', views.contacts, name='contacts'),
    path('creators', views.creators, name='creators'),
    path('author', views.author, name='author'),
    path('search', views.search, name='search'),
    path('', views.index, name='index'),
]
