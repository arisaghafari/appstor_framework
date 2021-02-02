from django.urls import path
from .views import *

app_name = "apps"
urlpatterns = [
    path('', home, name = "home"),
    path('app/<slug:slug>', AppDetail, name = "app_detail"),
]