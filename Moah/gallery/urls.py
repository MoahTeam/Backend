from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from posts.views import index


from gallery.views import Feb, Jan

app_name = 'gallery'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls', namespace='accounts')),

    path('jan/', Jan.as_view(), name='jan'),
    path('feb/', Feb.as_view(), name='feb'),
    path('mar/', Feb.as_view(), name='mar'),
    path('apr/', Feb.as_view(), name='apr'),
    path('may/', Feb.as_view(), name='may'),
    path('jun/', Feb.as_view(), name='jun'),
    path('jul/', Feb.as_view(), name='jul'),
    path('aug/', Feb.as_view(), name='aug'),
    path('sep/', Feb.as_view(), name='sep'),
    path('oct/', Feb.as_view(), name='oct'),
    path('nov/', Feb.as_view(), name='nov'),
    path('dec/', Feb.as_view(), name='dec'),
    
    #path('', index, name='index'),
    #path('posts/', include('posts.urls', namespace='post')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)