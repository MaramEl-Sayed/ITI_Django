from django.db import models
from django.shortcuts import get_object_or_404
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255, blank=False, unique=True)
    
    description = models.TextField(null=False, blank=False, max_length=500)
    
    @classmethod
    def getallcourses(cls):
        return cls.objects.all()

    @classmethod
    def getcoursebyid(cls,id):
        return get_object_or_404(cls,id=id)

    
    def __str__(self):
        return self.name