from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_display, name='article_display'),
]
