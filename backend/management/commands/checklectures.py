from django.core.management.base import BaseCommand, CommandError
from backend.models import Lecture

from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        lectures = Lecture.objects.all()
        for lecture in lectures:
            print 'I m parsing date'
            threshold = datetime.now() - timedelta(hours=2)
            th = threshold.strftime('%Y-%m-%d %H:%M:%S')
            lect = lecture.lecture_date.strftime('%Y-%m-%d %H:%M:%S')
            dt_th = datetime.strptime(th, '%Y-%m-%d %H:%M:%S')
            dt_lect = datetime.strptime(lect, '%Y-%m-%d %H:%M:%S')
            delta = dt_lect - dt_th
            # check with range of 15minutes
            if timedelta(hours=2) < delta < timedelta(hours=2, minutes=15) and lecture.booked_participants < 3 and lecture.is_available:
                print 'cancel lecture'
                print lecture.lecture_date, lecture.is_available
                lecture.lecture_date = None
                lecture.is_available = False
                lecture.save()
            elif timedelta(hours=2) > delta and lecture.booked_participants < 3 and lecture.is_available:
                print 'WARNING: under 2hours threshold, customer may upset'
            else:
                print 'book participants ok'

