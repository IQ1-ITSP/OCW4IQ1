from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    path('^$', views.toppage),
    path('result/', views.search_and_result),
    path('lecture/', views.lecture, name='lecture'),
    path('department/', views.department_page, name='department'),
]
