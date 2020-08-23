from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('student',views.add,name='addtocsv'),
    path('record',views.record, name='record'),
    path('search',views.search, name='search'),
    path('find',views.find,name='find'),
    path('display',views.display, name='display'),
]
