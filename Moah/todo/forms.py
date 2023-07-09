from django import forms
from .models import Todo

# class TodoBaseForm(forms.Form):
#     CATEGORY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정'),
#     ]
#     image = forms.ImageField()
#     content = forms.CharField(widget=forms.Textarea) #위젯을 주면 칸이 넓어짐
#     #category = forms.ChoiceField(label='카테고리', choice=CATEGORY_CHOICES)

class TodoBaseForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

























# from django.core.exceptions import ValidationError
# class TodoCreateForm(TodoBaseForm):
#     class Meta(TodoBaseForm.Meta):
#         fields = ['image', 'content']

#         def clean_content(self):
#             data = self.cleaned_data['content']
#             if "비속어" == data:
#                 raise ValidationError("'비속어'는 사용하실 수 없습니다.")

# class TodoUpdateForm(TodoBaseForm):
#     class Meta(TodoBaseForm.Meta):
#         fields = ['image', 'content']

# class TodoDetailForm(TodoBaseForm):
#     def __init__(self, *args, **kwargs):
#         super(TodoDetailForm, self).__init__(*args, **kwargs)
#         for key in self.fields:
#             self.fields[key].widget.attrs['disabled'] = True
#     # class Meta(TodoBaseForm.Meta):
#     #     fields = ['image', 'content']