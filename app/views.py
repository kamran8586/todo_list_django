from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    name = request.user.username
    is_authenticate = request.user.is_authenticated
    return render(request, 'todo_list.html', {'todos': todos, 'username': name, 'is_login': is_authenticate})


def add_todo(request):
    # return render(request, 'add_todo.html', {})
    if request.method == 'POST':
        task = request.POST.get('task')
        print(task)
        user_id = request.user.id
        todo = Todo(task=task, completed=False, user_id=user_id)
        todo.save()
        return redirect('todo_list')


def about(request):
    is_authenticate = request.user.is_authenticated
    return render(request, 'about.html', {'is_login': is_authenticate, 'username': request.user.username})


def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    print(todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id).delete()
    return redirect('todo_list')


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        password = password1
        if password1 != password2:
            return render(request, 'register.html', {'message': 'password are not same'}, status=401)
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)

            return redirect('login')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_list')
    return render(request, 'login.html')
