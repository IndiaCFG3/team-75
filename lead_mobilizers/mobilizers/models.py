from django.db import models

# Create your models here.
class Status(models.Model):
    stat=models.CharField(max_length=20)
class Gender(models.Model):
    gen=models.CharField(max_length=15)
class Category(models.Model):
    name=models.CharField(max_length=30)
class City(models.Model):
    Name=models.CharField(max_length=30)
class Course(models.Model):
    Name=models.CharField(max_length=30)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
class Mobilizer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contactnumber=models.CharField(max_length=13)
class Learners(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contactnumber=models.CharField(max_length=13)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    age=models.IntegerField()
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    status=models.ForeignKey(Status,on_delete=models.CASCADE)
    mobilizer=models.ForeignKey(Mobilizer,on_delete=models.CASCADE)

    
