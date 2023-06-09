from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from .models import Cumple
# Create your views here.


def home(request):

    return render(request, 'home.html',)


def signup(request):

    if request.method == 'GET':
        print('enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')

            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existente'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })

    return render(request, 'signup.html', {
        'form': UserCreationForm
    })


def tasks(request):
    pending_tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html', {'pending_tasks': pending_tasks})

@login_required
def tasks_completed(request):
    completed_tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {'completed_tasks': completed_tasks})


@login_required
def create_task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                "error": 'Error al crear la tarea'
            })


@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': "Error actualizando Tareas"})


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:  # Verifica si el usuario no es nulo
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Nombre de usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')


@login_required
def cumple(request):
    cumple_list = Cumple.objects.filter(user=request.user)  # Filtrar los cumpleaños por el usuario actual
    return render(request, 'cumple.html', {'cumple_list': cumple_list})


@login_required
def agregarCumple(request):
    cumple_list = Cumple.objects.filter(user=request.user)  # Filtrar los cumpleaños por el usuario actual

    if request.method == 'GET':
        return render(request, 'agregarCumple.html', {
            'form': CumpleForm,
            'cumple_list': cumple_list
        })
    else:
        try:
            form = CumpleForm(request.POST)
            new_cumple = form.save(commit=False)
            new_cumple.user = request.user
            new_cumple.save()
            return redirect('cumple')
        except ValueError:
            return render(request, 'agregarCumple.html', {
                'form': CumpleForm,
                'cumple_list': cumple_list,
                "error": 'Error al crear el cumpleaños'
            })
@login_required
def delete_cumple(request, cumple_id):
    cumple = get_object_or_404(Cumple, pk=cumple_id, user=request.user)
    if request.method == 'POST':
        cumple.delete()
        return redirect('cumple')