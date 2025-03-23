from django.urls import path
from . import views

urlpatterns = [
    path('', views.consults_view, name='consults'),
    path('start-consult/<int:appointment_id>/', views.start_consult, name='start-consult'),
    path('edit-consult/<int:consult_id>/', views.edit_consult, name='edit-consult')
]