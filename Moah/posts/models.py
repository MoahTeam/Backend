from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    checkbox = models.BooleanField(verbose_name="체크", default=False)
    todolist = models.TextField(verbose_name='내용')

