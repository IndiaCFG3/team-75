from django.db import models

# Create your models here.
class Status(models.Model):
    stat=models.CharField(max_length=20)
    def __str__(self):
        return '%s' % (self.stat)
class Gender(models.Model):
    gen=models.CharField(max_length=15)
    def __str__(self):
        return '%s' % (self.gen)
class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.name)

class City(models.Model):
    Name=models.CharField(max_length=30)
    def __str__(self):
        return '%s' % (self.Name)

class Course(models.Model):
    Name=models.CharField(max_length=30)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.Name)
class Mobilizers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contactnumber=models.CharField(max_length=13) 
    email=models.EmailField(default='abc@abc.com')   
    def __str__(self):
        return '%s' % (self.first_name)

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
    mobilizer=models.ForeignKey(Mobilizers,on_delete=models.CASCADE)
    def __str__(self):
        return '%s' % (self.first_name)

class tasks(models.Model):
    name=models.CharField(max_length=30)
    descreption=models.TextField()
    mobilizers=models.ForeignKey(Mobilizers,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return '%s' % (self.name)