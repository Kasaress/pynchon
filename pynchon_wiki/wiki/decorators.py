from django.shortcuts import redirect


def page_in_development(view_func):
    def wrapped(request, *args, **kwargs):
        in_development_mode = True
        if in_development_mode:
            return redirect('wiki:in_development')
        return view_func(request, *args, **kwargs)
    return wrapped
