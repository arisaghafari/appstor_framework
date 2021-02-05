from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, App
from .forms import CommentForm 
from .models import Comment
from django.shortcuts import redirect

from django.db.models import Q

def home(request):
    context = {
        #"apps": App.objects.filter(status = 'n').order_by('-created'),
        "apps": App.objects.order_by('-created'),
    }
    return render(request, "apps/index.html", context)

def AppDetail(request, slug):
    if request.method == 'POST': 
        cf = CommentForm(request.POST or None) 
        if cf.is_valid(): 
            content = request.POST.get('content') 
            post=get_object_or_404(App, slug = slug)
            comment = Comment.objects.create(post = post, user = request.user, content = content) 
            comment.save() 
            #return redirect("/") 
    else: 
      cf = CommentForm() 
        
    context = {
        "app": get_object_or_404(App, slug = slug),
        'comment_form':cf,
    }
    return render(request, "apps/app_detail.html", context)

def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug = slug),
    }
    return render(request, "apps/category.html", context)


def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) 

            results= App.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'apps/search.html', context)

        else:
            return render(request, 'apps/search.html')

    else:
        return render(request, 'apps/search.html')



