from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def starting_view(request):
    """ Renders a starting page(introduction page) a User sees once entered on the app page """
    return render(request, 'core/starting_page.html')


@login_required()
def home_view(request, *args, **kwargs):
    data = {
        "current_user": request.user
    }
    return render(request, 'core/home.html', data)
