from django.shortcuts import render
from .models import Learners
learner_list = Learners.objects.all()
def statusupdate(request):
    if request.user.is_authenticated:
        if request.user.email==request.Learner.mobilizer.email:
            t = Learners.objects.get(id=request.learner.id)
            t.status=request.status
#add return
