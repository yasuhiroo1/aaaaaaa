from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('result', views.result, name='result')
]