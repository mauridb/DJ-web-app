from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^courses/$', views.course_list, name='list-course'),
    url(r'^courses/(?P<pk>\d+)/$', views.course_detail, name='detail-course'),
    url(r'^lectures/$', views.lecture_list, name='list-lecture'),
    url(r'^lectures/(?P<pk>\d+)/$', views.lecture_detail, name='detail-lecture'),
    url(r'^news/$', views.news_list, name='list-news'),
    url(r'^news/(?P<pk>\d+)/$', views.news_detail, name='detail-news'),

    # booking actions url
    url(r'lectures/(?P<pk>\d+)/booking', views.booking, name='booking-lecture'),
]
