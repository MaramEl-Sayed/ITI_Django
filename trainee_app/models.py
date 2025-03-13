from django.db import models
from course_app.models import Course  

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainees")
    
    def __str__(self):
        return f"{self.name} - {self.course.name}"