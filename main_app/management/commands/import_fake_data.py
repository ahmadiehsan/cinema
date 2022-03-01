from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction

User = get_user_model()


class Command(BaseCommand):
    help = 'Import fake data'

    def handle(self, *args, **options):
        with transaction.atomic():
            User.objects.create_user(
                username='admin', email='admin@example.com', password='asdfqwer', is_staff=True, is_superuser=True
            )

            # TODO (ehsan) import fake data

        print('Fake data imported!')
