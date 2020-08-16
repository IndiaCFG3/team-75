from django.shortcuts import render
from .models import Learners

def home(request):
    return render(request, 'index.html')

def activities(request):
    return render(request,'mobilizers/activites.html')

def create(request):
    return render(request,'mobilizers/create.html')

def leads(request):
    learner_list = list(Learners.objects.all())
    print(type(learner_list))
    abcd=[]

    for a in learner_list:
        email=a.mobilizer.email
        if request.user.email==email:
            abcd.append(a)
        print(email)
        print(request.user.email) 
    return render(request,'mobilizers/leads.html',{'learn':abcd})

