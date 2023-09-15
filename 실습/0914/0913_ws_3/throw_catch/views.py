from django.shortcuts import render

# Create your views here.
def throw(request):
    if request.GET.get('second'):
        second = request.GET.get('second')
        context = {
            'second' : second
        }
        return render(request,'throw_catch/throw.html',context)
    else:
        return render(request,'throw_catch/throw.html')

def catch(request):
    first = request.GET.get('first')
    context = {
        'first' : first
    }
    return render(request,'throw_catch/catch.html',context)