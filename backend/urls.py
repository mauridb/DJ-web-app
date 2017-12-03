from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CustomerViewSet, CourseViewSet, LectureViewSet

router_v1 = DefaultRouter()

router_v1.register(r'users', UserViewSet)
router_v1.register(r'customers', CustomerViewSet)
router_v1.register(r'courses', CourseViewSet)
router_v1.register(r'lectures', LectureViewSet)


urlpatterns = [
    url(r'v1/', include(router_v1.urls, namespace='api-root-v1', app_name='backend')),
    # url(r'v2/', include(router_v2.urls, namespace='api-root-v2')),
]
