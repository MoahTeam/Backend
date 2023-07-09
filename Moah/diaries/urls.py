from django.urls import path

from .views import diary_list_view, diary_post_view,diary_post_image

app_name = 'diaries'

urlpatterns = [
    path('post/', diary_post_view, name = 'diary-post'),
    path('post/<int:id>', diary_post_view, name = 'diary-post'),
    path('post/image', diary_post_image, name = 'diary-image'),
    path('list/<int:id>', diary_list_view, name= 'diary-list'),
    path('list/', diary_list_view, name= 'diary-list'),
]