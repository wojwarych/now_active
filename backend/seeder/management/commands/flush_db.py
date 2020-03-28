from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Flush Database'

    def handle(self, *args, **options):
        management.call_command('flush', interactive=False, allow_cascade=True)
