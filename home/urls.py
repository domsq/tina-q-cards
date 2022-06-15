from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # add URL to show privacy policy as discussed with mentor
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
]
