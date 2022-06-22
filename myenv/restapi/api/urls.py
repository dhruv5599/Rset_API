import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('',TestVIew.as_view(),name = 'home'),
    ]
