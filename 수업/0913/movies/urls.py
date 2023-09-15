from django.urls import path
from . import views  # 장고에서 경로를 다 표시하도록 권장하고 있음
# movies/~~~
app_name = 'movies'
urlpatterns = [
    path('index/', views.index, name='index'),  # movies/index/
    path('page1/', views.page1, name='page1'),  # movies/index/
]