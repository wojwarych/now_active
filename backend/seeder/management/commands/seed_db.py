import os

from django.core import management
from django.core.management.base import BaseCommand

from seeder.apps import SeederConfig

FIXTURES_DIR = f'{SeederConfig.name}/fixtures/'
FIXTURES = os.listdir(FIXTURES_DIR)


class Command(BaseCommand):
    help = 'Seed Database'

    def handle(self, *args, **options):
        print(FIXTURES)
        management.call_command('loaddata', *FIXTURES)
