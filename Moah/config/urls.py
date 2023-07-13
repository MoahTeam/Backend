from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from posts.views import index

from config.views import Main
from config.views import Todo
from config.views import Diary
from config.views import Event
from config.views import Gallery
from todo.views import todo_create_view, todo_new_view, djangocreate, moahtodo, main

urlpatterns = [
    path('', Main.as_view(),name='main'),
    path('main/', main, name='main'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('gallery/',Gallery.as_view(),name='gallery'),
    
    path('todo/', Todo.as_view(),name='todo'),
    path('todo/',include('todo.urls', namespace='todo')),

    path('todo/new/', todo_new_view, name='todo-new'),
    path('todo/create/', todo_create_view, name='todo-create'),
    path('todo/moahtodo/', moahtodo, name='moahtodo'),
    path('todo/djangocreate/', djangocreate, name='djangocreate'),

    path('diary/', include('diaries.urls', namespace='diaries')),
    #path('diary/',Diary.as_view(),name='diary'),
    path('event/',Event.as_view(),name='event'),


    path('summernote/', include('django_summernote.urls')),
    
    #path('', index, name='index'),
    #path('posts/', include('posts.urls', namespace='post')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)