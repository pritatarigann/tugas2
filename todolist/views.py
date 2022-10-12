from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.core import serializers


def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created an account')
            return redirect('todolist:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist_ajax')
        else:
            messages.info(request, 'Username or password is wrong')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_data = Task.objects.filter(user = request.user)
    context = {
        'task_list': task_data,
        'username': request.user,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('taskname')
        description = request.POST.get('taskdesc')
        task = Task.objects.create(user=user, title=title, description=description)
        messages.success(request, "Successfully add new task")
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'new_task.html', context)

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    deleted_task = Task.objects.get(id=id)
    deleted_task.delete() 
    return redirect('todolist:show_todolist_ajax')

@login_required(login_url='/todolist/login/')
def update_status(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.is_finished = not task.is_finished
        task.save()
    else:
        messages.info(request, "You can't change the status of this task")
    return redirect('todolist:show_todolist_ajax')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    context = {
        'username': request.user,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task_ajax(request):
    if request.POST.get('action') == 'post':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(user=user, title=title, description=description)
        return JsonResponse({'status':'Done'})
    else:
        return JsonResponse({'status': 'Failed'}, status=400)

@login_required(login_url='/todolist/login/')
def delete_ajax(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.delete()
        return JsonResponse({'status': 'Done'})
    else:
        messages.info(request, "Failed")
        return JsonResponse({'status': 'Invalid deletion'}, status=403)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

    