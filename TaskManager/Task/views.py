from django.shortcuts import render,get_object_or_404,redirect
from.models import Task
from.forms import TaskForm
from django.http import Http404


def task_list(request):
    tasks = Task.objects.all()
    return (render(request, 'task_list.html', {'tasks': tasks}))

def task_create(request):
    if request.method == 'POST':
        form = TaskForm (request. POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'task_form.html', {'form': form})



def task_edit(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404("Task not found")

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        if request.method == 'POST':
            task.delete()
            return redirect('task_list')
    except Exception as e:
        return render(request, 'tasks/error.html', {'message': f"Error deleting task: {e}"})

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Create your views here.
