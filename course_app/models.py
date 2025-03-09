from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    
    description = models.TextField(null=False, blank=False, max_length=500)
