from django.conf.urls import url
from . import views

app_name = 'app'
urlpatterns = [
    #url(r'^$', views.test_response),
    url('^$', views.toppage),
    url('result/', views.search_and_result),
	url('lecture/',views.lecture,name='lecture'),
	url('department/',views.department_page,name='department'),
]
