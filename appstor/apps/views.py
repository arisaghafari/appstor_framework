from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def home(request):
    context = {
        "apps": App.objects.filter(status = 'n').order_by('-created')
    }
    return render(request, "apps/index.html", context)

def AppDetail(request, slug):
    context = {
        "app": get_object_or_404(App, slug = slug)
    }
    return render(request, "apps/app_detail.html", context)
