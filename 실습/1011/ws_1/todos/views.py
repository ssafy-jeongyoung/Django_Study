from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from accounts.models import User
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    return render(request,'todos/index.html',context)

def create(request):
    if request.method == "POST":
        user = User.objects.all()
        author = user.username
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = author
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form' : form
    }
    return render(request,'todos/create.html',context)