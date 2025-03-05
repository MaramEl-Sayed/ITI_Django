from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # duration = models.IntegerField()  # ✅ Add this field
