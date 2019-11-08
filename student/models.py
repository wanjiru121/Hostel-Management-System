from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User,default=None,null=True,on_delete=models.CASCADE)
    gender_choices = [('M','Male'),('F','Female')]
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField(max_length = 10,help_text = 'format : YYYY-MM-DD')
    gender = models.CharField(choices = gender_choices,max_length = 1)
    enrollment_number = models.CharField(max_length = 10,unique = True,null = True)
    course = models.ForeignKey('course.Course',null=True,default=None,on_delete=models.CASCADE)
    room_alloted = models.BooleanField(default = False)
    def __str__(self):
        return self.first_name

