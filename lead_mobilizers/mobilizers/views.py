from django.shortcuts import render
from .models import Learners,tasks

def home(request):
    return render(request, 'index.html')

def activities(request):
    activities_list=list(tasks.objects.all())
    abc=[]
    for b in activities_list:
        email=b.mobilizers.email
        if request.user.email==email:
            abc.append(b)
    return render(request,'mobilizers/activites.html',{'learn':abc}) 
    

def create(request):
    return render(request,'mobilizers/create.html')

def leads(request):
    learner_list = list(Learners.objects.all())
    
    abcd=[]

    for a in learner_list:
        email=a.mobilizer.email
        if request.user.email==email:
            abcd.append(a)
        
    return render(request,'mobilizers/leads.html',{'learn':abcd}) 

def leadstrack(request):
    return render(request,'mobilizers/leadstrack.html')

def mobilizerbasic(request):
    return render(request,'mobilizers/mobilizerbasic.html')

def timetable(request):
    return render(request,'mobilizers/timetable.html')

def login(request):
    return render(request,'mobilizers/login.html')

