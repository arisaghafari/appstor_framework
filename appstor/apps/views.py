from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        "apps":[
            {
                "title":"arisa",
                "description":"arisa's first app",
                "img":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fde.wikipedia.org%2Fwiki%2FApp_Store_(iOS)&psig=AOvVaw2UrVn1RZx1fMsOibu4iLAs&ust=1612174167504000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCMCmvv32xe4CFQAAAAAdAAAAABAD", 
            }
        ]
    }
    return render(request, "apps/home.html", context)

