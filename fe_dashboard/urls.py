from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^courses/$', views.course_list, name='list'),
    url(r'^courses/(?P<pk>\d+)/$', views.course_detail, name='detail'),
]
