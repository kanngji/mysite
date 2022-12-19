from django.urls import path

from . import views
urlpatterns = [
    # ''쓰는 이유 => config/urls.py 파일에서 이미
    # pybo/ 로 시작하는 URL이 pybo/urls.py 파일과 먼저 매핑

    path('', views.index),
    path('<int:question_id>/', views.detail),
]