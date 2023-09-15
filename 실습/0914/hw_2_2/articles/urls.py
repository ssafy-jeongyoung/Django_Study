from django.urls import path
from . import views

app_name ='articles'
# 나중에 url을 이름으로 가져다 쓸때, 명확하게 구분하기 위해서
# 이름 공간을 지정
urlpatterns = [
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
]
