import datetime
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.core.files import File

from apps.shop.models import Room, Seat, Movie

User = get_user_model()


class Command(BaseCommand):
    help = 'Import fake data'

    rooms = [
        Room(
            name='Red',
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        ),
        Room(
            name='Blue',
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        ),
        Room(
            name='Green',
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        ),
        Room(
            name='Yellow',
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
        )
    ]

    def handle(self, *args, **options):
        with transaction.atomic():
            self._generate_superuser()
            self._generate_rooms()
            self._generate_seates()
            self._generate_movies()

        # TODO (ehsan) import fake data

        print('Fake data imported!')

    @staticmethod
    def _generate_superuser():
        User.objects.create_user(
            username='admin', email='admin@example.com', password='asdfqwer', is_staff=True, is_superuser=True
        )

    def _generate_rooms(self):
        Room.objects.bulk_create(self.rooms)

    def _generate_seates(self):
        seats = [
            # Room Red
            Seat(room=self.rooms[0], row=1, number=1),
            Seat(room=self.rooms[0], row=1, number=2),
            Seat(room=self.rooms[0], row=1, number=3),
            Seat(room=self.rooms[0], row=1, number=4),
            Seat(room=self.rooms[0], row=1, number=5),
            Seat(room=self.rooms[0], row=1, number=6),
            Seat(room=self.rooms[0], row=1, number=7),
            Seat(room=self.rooms[0], row=1, number=8),
            Seat(room=self.rooms[0], row=1, number=9),
            Seat(room=self.rooms[0], row=2, number=1),
            Seat(room=self.rooms[0], row=2, number=3),
            Seat(room=self.rooms[0], row=2, number=4),
            Seat(room=self.rooms[0], row=2, number=5),
            Seat(room=self.rooms[0], row=2, number=7),
            Seat(room=self.rooms[0], row=2, number=8),
            Seat(room=self.rooms[0], row=2, number=9),
            Seat(room=self.rooms[0], row=3, number=1),
            Seat(room=self.rooms[0], row=3, number=2),
            Seat(room=self.rooms[0], row=3, number=3),
            Seat(room=self.rooms[0], row=3, number=4),
            # Room Blue
            Seat(room=self.rooms[1], row=1, number=1),
            Seat(room=self.rooms[1], row=1, number=2),
            Seat(room=self.rooms[1], row=1, number=3),
            Seat(room=self.rooms[1], row=2, number=1),
            Seat(room=self.rooms[1], row=2, number=2),
            Seat(room=self.rooms[1], row=2, number=3),
            Seat(room=self.rooms[1], row=3, number=1),
            Seat(room=self.rooms[1], row=3, number=2),
            Seat(room=self.rooms[1], row=3, number=3),
            Seat(room=self.rooms[1], row=4, number=1),
            Seat(room=self.rooms[1], row=4, number=2),
            Seat(room=self.rooms[1], row=4, number=3),
            # Room Green
            Seat(room=self.rooms[2], row=1, number=1),
            Seat(room=self.rooms[2], row=1, number=2),
            Seat(room=self.rooms[2], row=2, number=1),
            Seat(room=self.rooms[2], row=2, number=2),
            Seat(room=self.rooms[2], row=3, number=1),
            Seat(room=self.rooms[2], row=3, number=3),
            Seat(room=self.rooms[2], row=4, number=2),
            Seat(room=self.rooms[2], row=4, number=3),
            # Room Yellow
            Seat(room=self.rooms[3], row=1, number=1),
            Seat(room=self.rooms[3], row=1, number=2),
            Seat(room=self.rooms[3], row=1, number=3),
            Seat(room=self.rooms[3], row=1, number=4),
            Seat(room=self.rooms[3], row=1, number=5),
            Seat(room=self.rooms[3], row=2, number=1),
            Seat(room=self.rooms[3], row=2, number=2),
            Seat(room=self.rooms[3], row=2, number=4),
            Seat(room=self.rooms[3], row=2, number=5),
            Seat(room=self.rooms[3], row=3, number=1),
            Seat(room=self.rooms[3], row=3, number=2),
            Seat(room=self.rooms[3], row=3, number=3),
            Seat(room=self.rooms[3], row=3, number=4),
            Seat(room=self.rooms[3], row=3, number=5),
        ]

        Seat.objects.bulk_create(seats)

    def _generate_movies(self):
        poster_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'posters')
        posters = [
            {
                'name': '1.jpg',
                'file': File(open(os.path.join(poster_dir, '1.jpg'), 'rb')),
            },
            {
                'name': '2.jpg',
                'file': File(open(os.path.join(poster_dir, '2.jpg'), 'rb')),
            },
            {
                'name': '3.jpg',
                'file': File(open(os.path.join(poster_dir, '3.jpg'), 'rb')),
            },
            {
                'name': '4.jpg',
                'file': File(open(os.path.join(poster_dir, '4.jpg'), 'rb')),
            },
        ]
        movies = [
            # Room Red
            Movie(
                room=self.rooms[0],
                title='The Shawshank Redemption (1994)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(8, 0, 0),
                release_end_at=datetime.time(11, 0, 0),
            ),
            Movie(
                room=self.rooms[0],
                title='The Godfather (1972)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(12, 0, 0),
                release_end_at=datetime.time(15, 0, 0),
            ),
            Movie(
                room=self.rooms[0],
                title='The Dark Knight (2008)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(16, 0, 0),
                release_end_at=datetime.time(19, 0, 0),
            ),
            Movie(
                room=self.rooms[0],
                title='12 Angry Men (1957)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(20, 0, 0),
                release_end_at=datetime.time(23, 0, 0),
            ),
            # Room Blue
            Movie(
                room=self.rooms[1],
                title='The Shawshank Redemption (1994)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(8, 0, 0),
                release_end_at=datetime.time(11, 0, 0),
            ),
            Movie(
                room=self.rooms[1],
                title='The Godfather (1972)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(12, 0, 0),
                release_end_at=datetime.time(15, 0, 0),
            ),
            Movie(
                room=self.rooms[1],
                title='The Dark Knight (2008)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(16, 0, 0),
                release_end_at=datetime.time(19, 0, 0),
            ),
            Movie(
                room=self.rooms[1],
                title='12 Angry Men (1957)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(20, 0, 0),
                release_end_at=datetime.time(23, 0, 0),
            ),
            # Room Green
            Movie(
                room=self.rooms[2],
                title='The Shawshank Redemption (1994)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(8, 0, 0),
                release_end_at=datetime.time(11, 0, 0),
            ),
            Movie(
                room=self.rooms[2],
                title='The Godfather (1972)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(12, 0, 0),
                release_end_at=datetime.time(15, 0, 0),
            ),
            Movie(
                room=self.rooms[2],
                title='The Dark Knight (2008)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(16, 0, 0),
                release_end_at=datetime.time(19, 0, 0),
            ),
            Movie(
                room=self.rooms[2],
                title='12 Angry Men (1957)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(20, 0, 0),
                release_end_at=datetime.time(23, 0, 0),
            ),
            # Room Yellow
            Movie(
                room=self.rooms[3],
                title='The Shawshank Redemption (1994)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(8, 0, 0),
                release_end_at=datetime.time(11, 0, 0),
            ),
            Movie(
                room=self.rooms[3],
                title='The Godfather (1972)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(12, 0, 0),
                release_end_at=datetime.time(15, 0, 0),
            ),
            Movie(
                room=self.rooms[3],
                title='The Dark Knight (2008)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(16, 0, 0),
                release_end_at=datetime.time(19, 0, 0),
            ),
            Movie(
                room=self.rooms[3],
                title='12 Angry Men (1957)',
                description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
                release_date=timezone.now().date(),
                release_start_at=datetime.time(20, 0, 0),
                release_end_at=datetime.time(23, 0, 0),
            ),
        ]

        poster_index = 0
        for movie in movies:
            movie.poster.save(
                f"{movie.room.name}__{posters[poster_index]['name']}",
                posters[poster_index]['file']
            )
            movie.save()

            if poster_index == 3:
                poster_index = 0
            else:
                poster_index += 1
