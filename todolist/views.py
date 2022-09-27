# Mengimpor modul-modul yang diperlukan
from time import strftime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.task_form import TaskForm
from todolist.models import Task
import pytz

# user registration
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # add to database
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# user login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # Membuat response
            timezone = pytz.timezone('Asia/Jakarta')
            response.set_cookie('last_login', str(datetime.datetime.now(tz = timezone))) # create cookie last_login 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# user logout
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/') # restrict
# todolist 
def show_todolist(request):
    username = request.user.username
    user_id = request.user.id
    data_todolist = Task.objects.filter(user_id=user_id) # save data

    context = { 
        "username": username,
        "todolist": data_todolist
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/') # restrict
# add tasks
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid(): # requirements fulfilled
            task = Task(
                user = request.user,
                title = form.cleaned_data['judul'], 
                description = form.cleaned_data['deskripsi'],
            )
            task.save() # save task
            return HttpResponseRedirect(reverse("todolist:show_todolist"))
    else:
        form = TaskForm()
    
    context = {'form':form}
    return render(request, "create_task.html", context)

@login_required(login_url='/todolist/login/')
# delete task
def delete_task(request, id):
	deleted_task = Task.objects.get(id=id) # get task
	deleted_task.delete() # delete task 

	return HttpResponseRedirect("/todolist")

#resource: https://www.w3schools.com/django/django_delete_record.php

@login_required(login_url='/todolist/login/')
# update tasks state
def update_state(request, id):
    updated_task = Task.objects.get(id=id)

    if updated_task.is_finished:
        updated_task.is_finished = False
    else:
        updated_task.is_finished = True
    
    updated_task.save() # save
    return HttpResponseRedirect("/todolist")