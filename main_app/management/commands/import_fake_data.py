import datetime
import os

from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.shop.models import Room, Seat, Movie, Release

User = get_user_model()


class Command(BaseCommand):
    help = 'Import fake data'

    output_message_data = []

    rooms = [
        Room(
            name='One',
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
            color=Room.Color.RED
        ),
        Room(
            name='Two',
            description="Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin. Vehicula ipsum a arcu cursus vitae congue mauris rhoncus. Nisi vitae suscipit tellus mauris a diam maecenas. Gravida dictum fusce ut placerat orci nulla pellentesque. Quam pellentesque nec nam aliquam. Vel pharetra vel turpis nunc eget. Fermentum posuere urna nec tincidunt. Tortor condimentum lacinia quis vel eros donec ac. Ac orci phasellus egestas tellus rutrum.",
            color=Room.Color.BLUE
        ),
        Room(
            name='Three',
            description="Vitae nunc sed velit dignissim sodales ut eu. Nunc scelerisque viverra mauris in. Mi tempus imperdiet nulla malesuada pellentesque elit eget.",
            color=Room.Color.GREEN
        ),
        Room(
            name='Four',
            description="Mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare. Amet dictum sit amet justo donec enim diam vulputate. Dignissim suspendisse in est ante in nibh mauris cursus mattis. Quis lectus nulla at volutpat diam. At imperdiet dui accumsan sit amet nulla facilisi morbi tempus.",
            color=Room.Color.YELLOW
        )
    ]

    movies = [
        Movie(
            title='The Shawshank Redemption (1994)',
            description="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s",
        ),
        Movie(
            title='The Godfather (1972)',
            description="Tincidunt nunc pulvinar sapien et ligula ullamcorper malesuada proin. Vehicula ipsum a arcu cursus vitae congue mauris rhoncus. Nisi vitae suscipit tellus mauris a diam maecenas. Gravida dictum fusce ut placerat orci nulla pellentesque. Quam pellentesque nec nam aliquam. Vel pharetra vel turpis nunc eget. Fermentum posuere urna nec tincidunt. Tortor condimentum lacinia quis vel eros donec ac. Ac orci phasellus egestas tellus rutrum.",
        ),
        Movie(
            title='The Dark Knight (2008)',
            description="Vitae nunc sed velit dignissim sodales ut eu. Nunc scelerisque viverra mauris in. Mi tempus imperdiet nulla malesuada pellentesque elit eget.",
        ),
        Movie(
            title='12 Angry Men (1957)',
            description="Mattis ullamcorper velit sed ullamcorper morbi tincidunt ornare. Amet dictum sit amet justo donec enim diam vulputate. Dignissim suspendisse in est ante in nibh mauris cursus mattis. Quis lectus nulla at volutpat diam. At imperdiet dui accumsan sit amet nulla facilisi morbi tempus.",
        ),
    ]

    def handle(self, *args, **options):
        with transaction.atomic():
            self._generate_superuser()
            self._generate_rooms()
            self._generate_seates()
            self._generate_movies()
            self._generate_releases()
            self._print_output()

    def _generate_superuser(self):
        password = User.objects.make_random_password()
        username = 'admin'
        email = 'admin@example.com'

        self.output_message_data.append({
            'title': 'Login Credentials:',
            'data': {
                'username': username,
                'email': email,
                'password': password,
            }
        })

        User.objects.create_user(
            username=username, email=email, password=password, is_staff=True, is_superuser=True
        )

    def _generate_rooms(self):
        Room.objects.bulk_create(self.rooms)

    def _generate_seates(self):
        seats = [
            # Room One
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
            # Room Two
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
            # Room Three
            Seat(room=self.rooms[2], row=1, number=1),
            Seat(room=self.rooms[2], row=1, number=2),
            Seat(room=self.rooms[2], row=2, number=1),
            Seat(room=self.rooms[2], row=2, number=2),
            Seat(room=self.rooms[2], row=3, number=1),
            Seat(room=self.rooms[2], row=3, number=3),
            Seat(room=self.rooms[2], row=4, number=2),
            Seat(room=self.rooms[2], row=4, number=3),
            # Room Four
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

        poster_index = 0
        for movie in self.movies:
            movie.poster.save(
                movie.title,
                posters[poster_index]['file']
            )
            movie.save()

            if poster_index == 3:
                poster_index = 0
            else:
                poster_index += 1

    def _generate_releases(self):
        releases = [
            # Room One
            Release(
                room=self.rooms[0],
                movie=self.movies[0],
                date=timezone.localtime().date(),
                start_at=datetime.time(8, 0, 0),
                end_at=datetime.time(11, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[1],
                date=timezone.localtime().date(),
                start_at=datetime.time(12, 0, 0),
                end_at=datetime.time(15, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[2],
                date=timezone.localtime().date(),
                start_at=datetime.time(16, 0, 0),
                end_at=datetime.time(19, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[3],
                date=timezone.localtime().date(),
                start_at=datetime.time(20, 0, 0),
                end_at=datetime.time(23, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[0],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(8, 0, 0),
                end_at=datetime.time(11, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[1],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(12, 0, 0),
                end_at=datetime.time(15, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[2],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(16, 0, 0),
                end_at=datetime.time(19, 0, 0),
            ),
            Release(
                room=self.rooms[0],
                movie=self.movies[3],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(20, 0, 0),
                end_at=datetime.time(23, 0, 0),
            ),
            # Room Two
            Release(
                room=self.rooms[1],
                movie=self.movies[1],
                date=timezone.localtime().date(),
                start_at=datetime.time(12, 0, 0),
                end_at=datetime.time(15, 0, 0),
            ),
            Release(
                room=self.rooms[1],
                movie=self.movies[2],
                date=timezone.localtime().date(),
                start_at=datetime.time(16, 0, 0),
                end_at=datetime.time(19, 0, 0),
            ),
            Release(
                room=self.rooms[1],
                movie=self.movies[3],
                date=timezone.localtime().date(),
                start_at=datetime.time(20, 0, 0),
                end_at=datetime.time(23, 0, 0),
            ),
            Release(
                room=self.rooms[1],
                movie=self.movies[1],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(12, 0, 0),
                end_at=datetime.time(15, 0, 0),
            ),
            Release(
                room=self.rooms[1],
                movie=self.movies[2],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(16, 0, 0),
                end_at=datetime.time(19, 0, 0),
            ),
            Release(
                room=self.rooms[1],
                movie=self.movies[3],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(20, 0, 0),
                end_at=datetime.time(23, 0, 0),
            ),
            # Room Three
            Release(
                room=self.rooms[2],
                movie=self.movies[0],
                date=timezone.localtime().date(),
                start_at=datetime.time(8, 0, 0),
                end_at=datetime.time(11, 0, 0),
            ),
            Release(
                room=self.rooms[2],
                movie=self.movies[3],
                date=timezone.localtime().date(),
                start_at=datetime.time(20, 0, 0),
                end_at=datetime.time(23, 0, 0),
            ),
            Release(
                room=self.rooms[2],
                movie=self.movies[0],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(8, 0, 0),
                end_at=datetime.time(11, 0, 0),
            ),
            Release(
                room=self.rooms[2],
                movie=self.movies[3],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(20, 0, 0),
                end_at=datetime.time(23, 0, 0),
            ),
            # Room Four
            Release(
                room=self.rooms[3],
                movie=self.movies[2],
                date=timezone.localtime().date(),
                start_at=datetime.time(8, 0, 0),
                end_at=datetime.time(11, 0, 0),
            ),
            Release(
                room=self.rooms[3],
                movie=self.movies[2],
                date=timezone.localtime().date() + datetime.timedelta(1),
                start_at=datetime.time(8, 0, 0),
                end_at=datetime.time(11, 0, 0),
            ),
        ]

        Release.objects.bulk_create(releases)

    def _print_output(self):
        print('=========================')
        print('Fake data imported successfully!')
        print('-------------------------')
        for output in self.output_message_data:
            print(f"\n# {output['title']}")
            for item_key, item_value in output['data'].items():
                print(f'{item_key}: {item_value}')
        print('=========================')
