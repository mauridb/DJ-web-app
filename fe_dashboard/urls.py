from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'v2/', include(router_v2.urls, namespace='api-root-v2')),
]
