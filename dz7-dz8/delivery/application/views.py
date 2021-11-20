from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, resolve_url
from django.contrib.auth.views import redirect_to_login

from application import settings


def login_is_required(function=None, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    def wrap(request, *args, **kwargs):

        if request.user.is_authenticated:
            return function(request, *args, **kwargs)

        path = request.build_absolute_uri()
        resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)  # select valid login url
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]  # splitting login url into components
        current_scheme, current_netloc = urlparse(path)[:2]  # splitting current url into components
        if (not login_scheme or login_scheme == current_scheme) and \
                (not login_netloc or login_netloc == current_netloc):
            path = request.get_full_path()
        return redirect_to_login(path, resolved_login_url, redirect_field_name)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def rest_login_is_required(staff_required=False):

    def decorator_login_is_required(function=None, login_url=None,
                          redirect_field_name=REDIRECT_FIELD_NAME):

        def wrap(viewset, request, *args, **kwargs):

            if request.user.is_authenticated:
                if (staff_required and request.user.is_staff) or not staff_required:
                    return function(viewset, request, *args, **kwargs)

            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)  # select valid login url
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]  # splitting login url into components
            current_scheme, current_netloc = urlparse(path)[:2]  # splitting current url into components
            if (not login_scheme or login_scheme == current_scheme) and \
                    (not login_netloc or login_netloc == current_netloc):
                path = request.get_full_path()

            return redirect_to_login(path, resolved_login_url, redirect_field_name)

        wrap.__doc__ = function.__doc__
        wrap.__name__ = function.__name__
        return wrap

    return decorator_login_is_required


@login_is_required
def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')
