from django import forms
from .models import Todo

class TodoBaseForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class TodoForm(forms.Form):
    #checkbox = forms.BooleanField()
    todolist = forms.CharField(widget=forms.Textarea)
    #fields = ['checkbox', 'todolist']

