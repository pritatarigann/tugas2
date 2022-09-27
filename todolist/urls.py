from django.urls import path
from todolist.views import delete_task, show_todolist, register, login_user, logout_user, create_task, delete_task, update_state

app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('update-status/<int:id>', update_state, name='update_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
]