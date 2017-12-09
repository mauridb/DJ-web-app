# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .serializers import UserSerializer, CustomerSerializer, CourseSerializer, LectureSerializer
from .models import Customer, Course, Lecture
from django.contrib.auth.models import User


class UserViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_fields = ('first_name',)


class CustomerViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    model = Customer
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # filter_fields = ('type_customer',)


class CourseViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    model = Course
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # filter_fields = ('name',)


class LectureViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    model = Lecture
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    # filter_fields = ('theme',)

