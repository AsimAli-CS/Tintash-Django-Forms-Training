# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.get_name, name='get_name'),
    path('thanks/', views.thanks, name='thanks'),
]
