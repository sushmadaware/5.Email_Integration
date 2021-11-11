from django.urls import path
from .views import *

urlpatterns=[
    path('signup/',signup_view,name='signup'),
    path('adminview/', adminview, name='adminview'),
    path('log_in/',login_view,name='log_in'),
    path('log_out/',logout_view,name='log_out'),
]