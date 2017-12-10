from django.core.management.base import BaseCommand, CommandError
from backend.models import Lecture

from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        lectures = Lecture.objects.all()
        for lecture in lectures:
            threshold = datetime.now() - timedelta(hours=2)
            print threshold
            print lecture.lecture_date
            # TODO: to complete

