from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.index, name='index'),
    path('rainbow/', views.rainbow, name='rainbow'),
    path('rainbow/<chapter>/', views.rainbow_chapter, name='chapter'),
]