from django.db import models

# Create your models here.

class Post(models.Model):
    todolist = models.TextField(verbose_name='내용')