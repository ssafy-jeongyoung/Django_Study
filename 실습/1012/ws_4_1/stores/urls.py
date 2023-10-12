from django.urls import path, include
from . import views

app_name = "stores"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:pk>/', views.detail, name="detail"),
]