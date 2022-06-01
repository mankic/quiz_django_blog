from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_view, name='new'),
    path('detail/<int:pk>', views.detail_view, name='detail'),
    # detail_view 라는 함수가 PK라는 변수를 받아서 실행될 수 있게 되고
    path('<str:name>', views.article_view, name='article'),
    # article_view 라는 함수가 name 이라는 변수를 받아서 실행될 수 있다.
    path('',views.category_view, name='category'),
]