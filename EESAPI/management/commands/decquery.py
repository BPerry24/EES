from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Command to query DEC Database"

    def handle(self, *args, **options):
        pass
