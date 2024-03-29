from django.urls import path
from .views import AppDetail, category,home,searchposts

app_name = "apps"
urlpatterns = [
    path('', home, name = "home"),
    path('app/<slug:slug>', AppDetail, name = "app_detail"),
    path('category/<slug:slug>', category, name = "category"),
    path('search/', searchposts, name = "searchposts"),
]