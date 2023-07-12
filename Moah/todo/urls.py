
from django.urls import path
from .views import back_to_moahtodo, error_page, maincreate, success_page

from todo.views import  delete_button_view, djangocreate, moahtodo, todo_create_view, todo_list_view, todo_new_view, todo_save_view
app_name = 'todo'

urlpatterns = [
    #path('', todo_list_view, name='todo-list'),
    path('new/', todo_new_view, name='todo-new'),
    path('create/', todo_create_view, name='todo-create'),
    # path('<int:id>/edit', todo_update_view, name="todo-update"),
    # path('<int:id>/delete', todo_delete_view, name="todo-delete"),
    # path('save/', todo_save_view, name='todo-save'),
    path('moahtodo/delete/', delete_button_view, name='delete_button_view'),
    path('moahtodo/back_to_moahtodo/', back_to_moahtodo, name='back_to_moahtodo'),
    # path('moahtodo/delete2/', delete_button2_view, name='delete_button2_view'),
    # path('moahtodo/delete3/', delete_button3_view, name='delete_button3_view'),
    path('error_page/', error_page, name='error_page'),
    path('success_page/', success_page, name='success_page'),
    
]