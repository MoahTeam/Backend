from django import forms
from .models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

from django.core.exceptions import ValidationError  
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['todolist']

class PostUpdateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['todolist']