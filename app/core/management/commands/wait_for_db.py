# django command for ensuring database is ready

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        pass