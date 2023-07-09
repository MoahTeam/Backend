from django.urls import path

from todo.views import todo_create_view, todo_list_view, todo_new_view, todo_save_view
app_name = 'todo'

urlpatterns = [
    #path('', todo_list_view, name='todo-list'),
    path('new/', todo_new_view, name='todo-new'),
    path('create/', todo_create_view, name='todo-create'),
    # path('<int:id>/edit', todo_update_view, name="todo-update"),
    # path('<int:id>/delete', todo_delete_view, name="todo-delete"),
    # path('save/', todo_save_view, name='todo-save'),
]