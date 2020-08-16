from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    context = {
        'title':"Home Page"
    }
    return HttpResponse('<h1>Main Page</h1>')
