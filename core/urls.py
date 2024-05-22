"""
URL configuration for agriSoilCare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from core.view import pHAPI, pAPI, nAPI, kAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/pHmodel/', pHAPI.as_view(), name='pHmodel'),
    path('api/kmodel/', kAPI.as_view(), name='kmodel'),
    path('api/pmodel/', pAPI.as_view(), name='pmodel'),
    path('api/nmodel/', nAPI.as_view(), name='nmodel'),
]

