from django.views.generic import TemplateView

class Main(TemplateView):
    template_name ='main.html'
    
class Todo(TemplateView):
    template_name ='posts/moahtodo.html'
    
class Diary(TemplateView):
    template_name ='contact.html'
    
class Event(TemplateView):
    template_name ='portfolio.html'
    
class Gallery(TemplateView):
    template_name ='services.html'