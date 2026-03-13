from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Task, List
from .forms import UserForm, TaskForm, ListForm

# --- USERS ---
def user_list(request):
    users = User.objects.all()
    return render(request, 'task/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'task/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'task/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'task/user_confirm_delete.html', {'user': user})

# --- TASKS ---
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task/task_confirm_delete.html', {'task': task})

# --- LISTS ---
def list_list(request):
    lists = List.objects.all()
    return render(request, 'task/list_list.html', {'lists': lists})

def list_create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_list')
    else:
        form = ListForm()
    return render(request, 'task/list_form.html', {'form': form})

def list_update(request, pk):
    lista = get_object_or_404(List, pk=pk)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=lista)
        if form.is_valid():
            form.save()
            return redirect('list_list')
    else:
        form = ListForm(instance=lista)
    return render(request, 'task/list_form.html', {'form': form})

def list_delete(request, pk):
    lista = get_object_or_404(List, pk=pk)
    if request.method == 'POST':
        lista.delete()
        return redirect('list_list')
    return render(request, 'task/list_confirm_delete.html', {'list': lista})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def go_to_google(request):
    return redirect("https://www.google.com")