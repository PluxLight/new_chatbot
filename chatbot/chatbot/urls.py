"""chatbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app import views
from app import weathercrawl
from app import one_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu_up', views.menu_up),
    path('tomorrow_menu', views.tomorrow_menu),
    path('peri_list', views.peri_list),
    path('bistro', views.bistro),
    path('weather_print', weathercrawl.weather_print),
    path('room_print', one_room.room_print),

]
