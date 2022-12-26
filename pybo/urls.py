from django.urls import path

from . import views

app_name = 'pybo'
urlpatterns = [
    # ''쓰는 이유 => config/urls.py 파일에서 이미
    # pybo/ 로 시작하는 URL이 pybo/urls.py 파일과 먼저 매핑

    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]