from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('in_development', views.in_development, name='in_development'),
    path('rainbow/double_katie/', views.double_katie, name='double_katie'),
    path('rainbow/notes/<chapter_number>/', views.rainbow_notes,
         name='rainbow_notes'),
    path('rainbow/comments/<chapter_number>/', views.rainbow_comments,
         name='rainbow_comments'),
    path('rainbow_part1', views.rainbow_part1, name='rainbow_part1'),
    path('rainbow_part2', views.rainbow_part2, name='rainbow_part2'),
    path('rainbow_part3', views.rainbow_part3, name='rainbow_part3'),
    path('rainbow_part4', views.rainbow_part4, name='rainbow_part4'),
    path('rainbow_part5', views.rainbow_part5, name='rainbow_part5'),
    path('rainbow_part6', views.rainbow_part6, name='rainbow_part6'),
    path('rainbow_part7', views.rainbow_part7, name='rainbow_part7'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]
