from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from posts.views import index


from gallery.views import  Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec

app_name = 'gallery'
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls', namespace='accounts')),

    path('jan/', Jan.as_view(), name='jan'),
    path('feb/', Feb.as_view(), name='feb'),
    path('mar/', Mar.as_view(), name='mar'),
    path('apr/', Apr.as_view(), name='apr'),
    path('may/', May.as_view(), name='may'),
    path('jun/', Jun.as_view(), name='jun'),
    path('jul/', Jul.as_view(), name='jul'),
    path('aug/', Aug.as_view(), name='aug'),
    path('sep/', Sep.as_view(), name='sep'),
    path('oct/', Oct.as_view(), name='oct'),
    path('nov/', Nov.as_view(), name='nov'),
    path('dec/', Dec.as_view(), name='dec'),
    
    #path('', index, name='index'),
    #path('posts/', include('posts.urls', namespace='post')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)