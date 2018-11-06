from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path(r'', views.toppage),
    path('result/', views.search_and_result),
    path('lecture/', views.lecture, name='lecture'),
    path('department/', views.department_page, name='department'),
]
