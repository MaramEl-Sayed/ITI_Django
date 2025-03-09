from django.db import models

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
