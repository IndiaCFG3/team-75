from django.contrib import admin
from .models import Status,Gender,Category,City,Course,Mobilizers,Learners,tasks
admin.site.register(Status)
admin.site.register(Gender)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Course)
admin.site.register(Mobilizers)
admin.site.register(Learners)
admin.site.register(tasks)