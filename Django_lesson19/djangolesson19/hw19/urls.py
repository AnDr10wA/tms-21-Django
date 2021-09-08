from django.contrib import admin
from django.urls import path, include
from .views import aviaticket
urlpatterns = [

    path('form', aviaticket , name = 'avia_ticket')]