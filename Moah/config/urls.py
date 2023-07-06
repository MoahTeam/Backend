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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('', Main.as_view(),name='main'),
    path('todo/',Todo.as_view(),name='todo'),
    path('diary/', include('diaries.urls', namespace='diaries')),
    #path('diary/',Diary.as_view(),name='diary'),
    path('event/',Event.as_view(),name='event'),
    path('gallery/',Gallery.as_view(),name='gallery'),
    
    #path('', index, name='index'),
    #path('posts/', include('posts.urls', namespace='post')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)