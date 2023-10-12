from django.shortcuts import render, redirect
from .forms import StoreForm
from .models import Store
# Create your views here.
def index(request):
    stores = Store.objects.all()
    store_form = StoreForm()
    context = {
        'stores' : stores,
        'store_form' : store_form,
    }
    return render(request, 'stores/index.html', context)

def detail(request, pk):
    store = Store.objects.get(pk=pk)
    context = {
        'store' : store,
    }
    return render(request, 'stores/detail.html', context)