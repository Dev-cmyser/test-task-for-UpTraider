from django.urls import path
from .views import index, about, first, second, third










urlpatterns = [
    path('', index),
    path('about/', about, name='about'),
    path('first/', first, name='first'),
    path('second/', second, name='second'),
    path('third/', third, name='third'),
]
