"""Singhealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import home_view,contact_view,login_view,register_view,dashboard_view,logout_view,search_view
from uploadImage.views import image_view, success, display_images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('contact/',contact_view),
    path('login/',login_view,name= 'login'),
    path('register/',register_view,name ='register'),
    path('dashboard/',dashboard_view,name='dashboard'), 
    path('logout/',logout_view,name='logout'),   
    path('search/',search_view),
    path('image_upload/', image_view, name = 'image_upload'), 
    path('success/', success, name = 'success'), 
    path('display_images/', display_images, name = 'display_images'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
