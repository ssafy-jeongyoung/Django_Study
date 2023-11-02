
from django.urls import path, include
from . import views

urlpatterns = [
    # 날씨 API 테스트
    path('', views.index),
    # 서울의 5일치 예보 데이터 확인
    # path('', views.),
    # 예보 데이터 중 원하는 데이터만 DB에 저장
    # path('', views.),
    # 저장된 데이터 전체 조회
    # path('/', views.),
    # 특정조건 데이터 확인 : 30도 이상
    # path('/', views.),
]
