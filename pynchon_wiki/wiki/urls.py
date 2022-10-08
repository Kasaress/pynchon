from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.index, name='index'),
    path('rainbow/', views.rainbow, name='rainbow'),
    path('rainbow/<chapter_number>/', views.rainbow_chapter, name='chapter'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )