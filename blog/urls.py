from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_overview, name='blog_overview'),
]
