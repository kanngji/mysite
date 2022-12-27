
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
from pybo import views


# urls.py 파일은 페이지 요청이 발생하면 가장 먼저 호출되는 파일
# URL 과 뷰 함수 간의 매핑을 정의한다


urlpatterns = [
    path('admin/', admin.site.urls),
    # pybo/ URL이 요청되면 views.index를 호출하라는 매핑
    path('pybo/', include('pybo.urls')),
    # views.index는 views.py 파일의 index 함수를 의미한다
    # URL을 정규화하는 장고의 기능 URL 매핑시 항상 끝에 / 붙이기
    path('common/',include('common.urls')),
    path('', base_views.index, name='index'), # '/' 에 해당되는 path
]
