from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.test_response),
    url('^$', views.toppage),
    url('abc/', views.search_and_result),
]
