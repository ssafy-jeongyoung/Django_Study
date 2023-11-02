from django.urls import path
from . import views

app_name="boards"
urlpatterns = [
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'), 
    path('accounts/<int:user_pk>/follow/', views.follow, name="follow"),
]