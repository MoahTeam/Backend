from django.contrib import admin

from .models import Diary

@admin.register(Diary)
class UserModelAdmin(admin.ModelAdmin):
    pass
