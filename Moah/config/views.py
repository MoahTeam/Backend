from django.views.generic import TemplateView

from todo.forms import TodoForm

class Main(TemplateView):
    template_name ='main.html'
    
class Todo(TemplateView):
    template_name ='todo/moahtodo.html'
    
class Diary(TemplateView):
    template_name ='Diary/diary.html'
    
class Event(TemplateView):
    template_name ='event.html'
    
class Gallery(TemplateView):
    template_name ='Gallery/7.html'

