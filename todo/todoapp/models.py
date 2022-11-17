from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=50)
    detail=models.CharField(max_length=500)
    cat=models.CharField(max_length=10)
    date=models.DateField()
    is_deleted=models.CharField(max_length=5)
