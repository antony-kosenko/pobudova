from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import starting_view, home_view, last_bills_view
from .views import create_record_view

app_name = 'core'

urlpatterns = [
    path('', starting_view, name='start'),
    path('home/', home_view, name='home'),
    path('hub/', RedirectView.as_view(url=reverse_lazy('core:last_bills'), permanent=True)),
    path('hub/last-bills/', last_bills_view, name='last_bills'),
    path('hub/new-record/', create_record_view, name='create_record')

]
