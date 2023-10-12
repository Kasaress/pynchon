# from django.conf import settings
from django.shortcuts import render
# from django.contrib.admin.views.decorators import staff_member_required

# from services.time import get_datetime_today


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)


def csrf_failure(request):
    return render(request, 'core/403csrf.html')


def server_error(request):
    return render(request, 'core/500.html', status=500)


def permission_denied(request, exception):
    return render(request, 'core/403.html', status=403)


# @staff_member_required
# def log_view(request):
#     template = 'core/log.html'
#     with open(settings.LOG_FILE_NAME, 'r') as file:
#         context = {
#             'title': f'Лог {get_datetime_today()}',
#             'log': file.read()
#         }
#     return render(request, template, context)
