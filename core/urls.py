from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('', views.my_home, name='home'),
    path('register/', views.registration, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
]
