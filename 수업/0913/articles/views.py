from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def page1(request):
    return render(request, 'articles/page1.html')

def page2(request):
    return render(request, 'articles/page2.html')