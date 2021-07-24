from django.urls import path
from . import views

urlpatterns = [
    path('tcomment', views.tcomment, name='tcomment')
]