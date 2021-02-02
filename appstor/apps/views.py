from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    context = {
        "apps": App.objects.filter(status = 'n').order_by('-created')
    }
    return render(request, "apps/index.html", context)

def AppDetail(request, slug):
    context = {
        "app": App.objects.get(slug = slug)
    }
    return render(request, "apps/app_detail.html", context)
