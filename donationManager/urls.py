from main_app import views
from django.contrib import admin
from django.urls import path, re_path
from main_app import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.index)
]
