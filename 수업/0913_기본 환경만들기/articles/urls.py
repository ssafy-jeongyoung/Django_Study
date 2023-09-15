from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # articles/index/
    path('index/', views.index, name ='index'),
    path('catch/<str:name>/<int:number>', views.catch, name='catch')
]