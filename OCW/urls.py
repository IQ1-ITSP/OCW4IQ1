from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    path(r'', views.toppage),
    path(r'abc', views.search_and_result),
    path(r'lecture', views.lecture, name='lecture'),
    path(r'department', views.department_page, name='department'),
    #path(r'base_layout', views.base_layout, name='base_layout'),
]
