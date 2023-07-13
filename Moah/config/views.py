from django.views.generic import TemplateView
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.shortcuts import render

from todo.forms import TodoForm
from diaries.models import Diary, DiaryImage

class Main(TemplateView):
    template_name ='main.html'
    
class Todo(TemplateView):
    template_name ='todo/moahtodo.html'
    
class Event(TemplateView):
    template_name ='event.html'
    
class Gallery(TemplateView):
    template_name ='Gallery/7.html'


