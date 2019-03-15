from django.shortcuts import render
from time import localtime, strftime

def index(request):
    
    context = {
        "date" : strftime("%Y-%m-%d", localtime()),
        "time" : strftime("%I:%M %p", localtime())
    }


    return render(request, "first_app/index.html", context)