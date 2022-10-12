from django.urls import path
from todolist.views import create_task_ajax, delete_ajax, login_user, register, show_json, show_todolist_ajax, logout_user, create_task, delete_ajax, update_status, show_todolist_ajax, update_status


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create-task'),
    path('delete-task/<int:id>', delete_ajax, name='delete_task'),
    path('update-status/<int:id>', update_status, name='update_status'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show-json'),
    path('add/', create_task_ajax, name='create-task-ajax'),
]