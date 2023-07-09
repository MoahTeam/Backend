from django.db import models
from django.contrib.auth import get_user_model

from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

from datetime import datetime
from django.utils.dateformat import DateFormat

User = get_user_model()

class Diary(models.Model):
    FEEL_CHOICES = [
        ('1', "기쁨"),
        ('2', "행복"),
        ('3', "좋음"),
        ('4', "별로"),
        ('5', "화남"),
        ('6', "슬픔"),
        ('7', "보통"),
    ]
    #feeling 필수인지 없어도 되는지 물어보기
    feeling = models.CharField(verbose_name="기분", max_length=2, choices=FEEL_CHOICES, default=2)
    title = title = models.CharField(verbose_name="제목", max_length=80, default = '')
    content = models.TextField(verbose_name="내용", null=True, blank=True)
    created_at = models.DateTimeField("작성일", auto_now_add=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    secure = models.BooleanField(verbose_name="공개여부", null = False, default=True)

class DiaryImage(models.Model):
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField("업로드 날짜", auto_now_add=True)
    image = models.ImageField(default='', upload_to= "diary/"+datetime.now().strftime('%Y.%m.%d'), blank=True, null=True)

