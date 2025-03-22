from django.urls import path
from . import views

urlpatterns = [
    path('', views.consults_view, name='consults'),
]