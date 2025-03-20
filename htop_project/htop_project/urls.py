# htop_project/htop_project/urls.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from htop_app.views import htop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('htop/', htop, name='htop'),
    # Add a root path that redirects to the htop page
    path('', lambda request: redirect('htop'), name='root'),
]