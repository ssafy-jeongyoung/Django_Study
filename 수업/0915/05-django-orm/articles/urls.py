from django.urls import path
from . import views

app_name="articles"
urlpatterns = [
    # index, new, create, delete
    path('index/', views.index2, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]