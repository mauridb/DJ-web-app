# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from backend.models import Course, Lecture


def home(request):
    context = {

    }
    return render(request, 'home.html', context)


def course_list(request):
    courses = Course.objects.all()
    print request.method

    return render(request, 'fe_dashboard/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'fe_dashboard/course_detail.html', {'course': course})


def lecture_list(request):
    lectures = Lecture.objects.all()
    print request.method

    return render(request, 'fe_dashboard/lecture_list.html', {'lectures': lectures})


def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render(request, 'fe_dashboard/lecture_detail.html', {'lecture': lecture})

