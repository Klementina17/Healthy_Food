from django.db import models

# Create your models here.
class User(models.Model):
    username=models.TextField(max_length=10)
    password=models.TextField(max_length=50)
    repeat_password = models.TextField(max_length=50)
    age=models.TextField(max_length=2)
    weight=models.TextField(max_length=5)
    height = models.TextField(max_length=5)
    email=models.TextField(max_length=20)

