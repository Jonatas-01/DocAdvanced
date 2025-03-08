from . import views
from django.urls import path

urlpatterns = [
    path('', views.my_home, name='home'),
    path('register/', views.registration, name='register')
]
