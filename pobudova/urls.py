from django.contrib import admin
from django.urls import path, include


app_name = 'pobudova'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', include('core.urls')),
]
