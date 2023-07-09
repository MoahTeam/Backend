from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Todo(models.Model):
    #checkbox = models.BooleanField(verbose_name="체크", default=False)
    todolist = models.CharField(verbose_name='내용', max_length=100)
    #todolist = models.TextField(verbose_name='내용')
    #body = models.CharField(verbose_name='내용2', max_length=100)

