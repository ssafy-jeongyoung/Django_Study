from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def catch(request, name, number):
    # url에서 변수로 들어오는 값을 받아야 함.
    context = {
        'name' : name,
        'number' : number,
    }
    return render(request, 'articles/catch.html', context)