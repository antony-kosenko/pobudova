from django.shortcuts import render


# Create your views here.

def index_view(request, *args, **kwargs):
    return render(request, 'core/home.html', {})


def test_view(request, *args, **kwargs):
    return render(request, 'test.html', {})

