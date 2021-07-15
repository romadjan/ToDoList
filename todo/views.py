from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User




def task_list(request):

    user = request.user
    form = TaskForm()
    tasks = Task.objects.all()


    if request.method == "POST":

        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()

            form.save()
    context = {
        "title": "ToDo List",
        "tasks": tasks,
        "form": form
    }

    return render(request, "todo/list.html", context)


def update_task(request, pk):
    tasks = Task.objects.get(id = pk)
    form = TaskForm(instance=tasks)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        "title": "Update Task",
        "tasks": tasks,
        "form": form
    }
    return render(request, "todo/update.html", context)

def delete_task(request, pk):
    tasks = Task.objects.get(id = pk)
    if request.method == "POST":
        tasks.delete()
        return redirect("/")
    context = {
        "title": "Delete Task",
        "tasks": tasks,
    }
    return render(request, "todo/delete.html", context)



