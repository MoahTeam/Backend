from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from posts.views import index


from gallery.views import  gallery_view

app_name = 'gallery'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls', namespace='accounts')),

    path('', gallery_view, name="gallery-list"),
    path('<int:month>/<int:day>', gallery_view, name="gallery-list"),
    path('<int:day>', gallery_view, name="gallery-list"),
    path('<int:month>', gallery_view, name="gallery-list"),
    
    
    #path('', index, name='index'),
    #path('posts/', include('posts.urls', namespace='post')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)