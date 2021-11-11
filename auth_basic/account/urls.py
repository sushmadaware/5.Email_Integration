from django.urls import path
from .views import home,loginview,logoutview,registerview

urlpatterns=[
    path('',home,name='home'),
    path('v1/',loginview,name='login'),
    path('v2/',logoutview,name='logout'),
    path('v3/',registerview,name='register')
]