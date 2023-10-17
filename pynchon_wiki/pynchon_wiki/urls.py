from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

# import core.views

urlpatterns = [
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('captcha/', include('captcha.urls')),
    path('admin/', admin.site.urls),
    # path('log/', core.views.log_view),
    path('', include('wiki.urls')),
]

CSRF_FAILURE_VIEW = 'core.views.csrf_failure'
handler403 = 'core.views.permission_denied'
handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
