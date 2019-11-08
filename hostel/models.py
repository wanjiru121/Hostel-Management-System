from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length=5)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(choices=gender_choices,max_length=1,default=None,null=True)
    course = models.ManyToManyField('course.Course', default=None, blank=True)
    warden = models.CharField(max_length=100, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name