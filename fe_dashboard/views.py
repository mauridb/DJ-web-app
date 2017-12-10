# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404, redirect
from backend.models import Course, Lecture, Customer


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


def booking(request, pk):
    print request, pk
    customer = Customer.objects.get(web_user=request.user)
    lecture = Lecture.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST.get('booking') and customer.allow_booking is True and customer.count_booking <= customer.subscription.time_booking:
            # handle booking on lecture max participants
            if lecture.booked_participants < lecture.max_attendees:
                lecture.booked_participants += 1
                customer.count_booking += 1
                lecture.save()
                customer.save()
            else:
                print 'Lecture has been completed!'
        elif request.POST.get('booking') and customer.allow_booking is True and customer.count_booking > customer.subscription.time_booking:
            print 'Not allowed upgrade your subscription to advanced'
        elif request.POST.get('dismiss') and customer.allow_booking is True:
            customer.count_disclaimer += 1
            customer.count_booking -= 1
            lecture.booked_participants -= 1
            if customer.count_disclaimer > 2:
                customer.allow_booking = False
                customer.disable_date = datetime.now()
                customer.enable_date = customer.disable_date + timedelta(days=1)
                print customer.disable_date, customer.enable_date
            else:
                print 'Undesired Customer'
            customer.save()
            lecture.save()
        else:
            print 'Permission denied!'
    else:
        print 'Booking not allowed'

    return redirect('/web/lectures/')

