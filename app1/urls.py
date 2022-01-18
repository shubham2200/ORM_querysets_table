from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name='home'),
    path('show_data/' , show_data , name='show_data' ),
    # path('filter_django/', filter_django,name='filter_django' )
]
