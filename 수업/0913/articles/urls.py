from django.urls import path
from . import views  # 장고에서 경로를 다 표시하도록 권장하고 있음
# articles/~~~
app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),  # articles/index/
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]