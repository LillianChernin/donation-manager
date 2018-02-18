from main_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.index),
    path(r'donor/', views.donor_profile)
]
