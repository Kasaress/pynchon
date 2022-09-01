from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('rainbow/', views.rainbow),
    path('rainbow/<chapter>/', views.rainbow_chapter),
]