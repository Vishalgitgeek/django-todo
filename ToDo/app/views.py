from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Task added successfully! <br>  <a href = "/">Go to Home</a>')

    context = {'tasks': tasks, 'form': form}
    

    return render(request, 'app/index.html', context)


def update_task(request, task_id):
    task = Task.objects.get(id = task_id)
    form = TaskForm(instance = task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return HttpResponse('Task updated successfully' + '<br> <a href = "/">Go to Home</a>')
    context = {'form': form, 'task':task}
    return render(request, 'app/update_task.html', context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return HttpResponse('task deleted successfully  <a href = "/">Go to Home</a>')
    context = {'task': task}
    return render(request, 'app/delete_task.html', context)
