from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from accounts.models import User
# Create your views here.
def index(request):
    todos = request.user.todo_set.all()
    todo_form = TodoForm()
    context = {
        'todos' : todos,
        'todo_form' : todo_form,
    }
    return render(request,'todos/index.html',context)


def create(request):
    if request.method == "POST":
        author = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = author
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form' : form
    }
    return render(request,'todos/create.html',context)