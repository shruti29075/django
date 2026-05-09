from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Task

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        
        if password != password_confirm:
            return render(request, "todo/register.html", {"error": "Passwords don't match"})
        
        if User.objects.filter(username=username).exists():
            return render(request, "todo/register.html", {"error": "Username already exists"})
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("task_list")
    
    return render(request, "todo/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("task_list")
        else:
            return render(request, "todo/login.html", {"error": "Invalid credentials"})
    
    return render(request, "todo/login.html")

@login_required(login_url='login')
def task_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        completed = request.POST.get("completed") == "on"
        document = request.FILES.get("document")

        Task.objects.create(user=request.user, name=name, completed=completed, document=document)
        return redirect("task_list")

    tasks = Task.objects.filter(user=request.user).all()
    return render(request, "todo/task_list.html", {"tasks": tasks})

@login_required(login_url='login')
@require_http_methods(["POST"])
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect("task_list")

@login_required(login_url='login')
@require_http_methods(["POST"])
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect("login")
