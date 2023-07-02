from django.db import models

# Create your models here.

class Post(models.Model):
    checkbox = models.BooleanField(verbose_name="체크", default=False)
    todolist = models.TextField(verbose_name='내용')