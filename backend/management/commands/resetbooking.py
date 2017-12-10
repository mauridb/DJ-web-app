from django.core.management.base import BaseCommand, CommandError
from backend.models import Customer


class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        customers = Customer.objects.all().update(count_booking=0, count_disclaimer=0)

        self.stdout.write('Really simple!!')
