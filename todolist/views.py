from django.shortcuts import (render, redirect, get_object_or_404)
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, login, logout)
from todolist.models import Task
import datetime

@login_required(login_url='/todolist/login')
def show_todolist(request):
    data = Task.objects.filter(user=request.user)
    context = {
    'list_todo' : data,
    'username' :  request.user.username,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        status = False
        Task.objects.create(title=title, description=description, date=date, user=user, status=status)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response

    return render(request, "create.html")

def change_task(request, pk):
    data = Task.objects.get(id=pk)
    data.status = not(data.status)
    data.save()
    return redirect('todolist:show_todolist')

def delete_task(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

# Create your views here.