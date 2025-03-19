from django.db import models
from course_app.models import Course  
from django.shortcuts import get_object_or_404

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainees")

    @classmethod
    def getalltrainees(cls):
        return cls.objects.all()

    @classmethod
    def gettraineebyid(cls,id):
        return get_object_or_404(cls,id=id)
    
    def __str__(self):
        return f"{self.name} - {self.course.name}"