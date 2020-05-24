"""rsr_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', views.login),
    path('api/create_type', views.create_type),
    path('api/types', views.get_types),
    path('api/types/<int:type_id>', views.get_type_by_id),
    path('api/create_sign', views.create_sign),
    path('api/signs', views.get_signs),
    path('api/signs/<int:sign_id>', views.get_sign_by_id),
    path('api/signs/get_labels', views.get_labels),
]
