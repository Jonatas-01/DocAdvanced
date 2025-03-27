"""
URL configuration for docadvanced project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler403, handler500
from .errors import custom_404_view, custom_403_view, custom_500_view

handler404 = custom_404_view
handler403 = custom_403_view
handler500 = custom_500_view

urlpatterns = [
    path('', include('core.urls'), name="core"),
    path('account/', include('account.urls'), name="account"),
    path('appointments/', include('appointments.urls'), name='appointment-view'),
    path('consults/', include('consults.urls'), name='consults-view'),
    path('admin/', admin.site.urls),
]
