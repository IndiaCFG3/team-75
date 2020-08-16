from django.shortcuts import render,HttpResponse
from .models import Learners
learner_list = Learners.objects.all()

def home(request):
    return render(request, 'mobilizers/index.html')

def statusupdate(request):
    if request.user.is_authenticated:
        if request.user.email==request.Learner.mobilizer.email:
            t = Learners.objects.get(id=request.learner.id)
            t.status=request.status
#add return


def activities(request):
    return render(request,'mobilizers/activites.html')

def create(request):
    return render(request,'mobilizers/create.html')

def leads(request):
    return render(request,'mobilizers/leads.html')

def leadstrack(request):
    return render(request,'mobilizers/leadstrack.html')

def mobilizerbasic(request):
    return render(request,'mobilizers/mobilizerbasic.html')

def timetable(request):
    return render(request,'mobilizers/timetable.html')

def login(request):
    return render(request,'mobilizers/login.html')