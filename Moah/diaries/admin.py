from django.contrib import admin

from .models import Diary

@admin.register(Diary)
class DiaryModelAdmin(admin.ModelAdmin):
    list_display = ('feeling', 'content', 'title', 'secure', 'writer', 'id')
    #list_editable = ('content', )
    list_Filter=('created_at',)
    search_fields = ('id', 'writer__username',)
    readonly_fields = ('created_at',)
    search_help_text = ''

    actions = []
