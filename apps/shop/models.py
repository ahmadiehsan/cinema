from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from helpers.models import BaseModel

User = get_user_model()


class Room(BaseModel):
    class Color(models.TextChoices):
        RED = 'R', _('Red')
        BLUE = 'B', _('Blue')
        GREEN = 'G', _('Green')
        YELLOW = 'Y', _('Yellow')

    name = models.CharField(max_length=100, verbose_name=_('Name'), unique=True)
    description = models.TextField(verbose_name=_('Description'))
    color = models.CharField(max_length=2, choices=Color.choices, verbose_name=_('Color'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')


class Seat(BaseModel):
    room = models.ForeignKey(Room, related_name='seats', verbose_name=_('Room'), on_delete=models.CASCADE)
    row = models.PositiveSmallIntegerField(verbose_name=_('Row'))
    number = models.PositiveSmallIntegerField(verbose_name=_('Number'))

    def __str__(self):
        return f'{self.row}{self.number}'

    class Meta:
        unique_together = ('room', 'row', 'number')
        verbose_name = _('Seat')
        verbose_name_plural = _('Seats')


class Movie(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'), db_index=True, unique=True)
    description = models.TextField(verbose_name=_('Description'))
    poster = models.ImageField(upload_to='shop/movie/posters', verbose_name=_('Poster'))
    rooms = models.ManyToManyField(
        Room,
        through='Release',
        through_fields=('movie', 'room'),
        related_name='movies',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')


class Release(BaseModel):
    room = models.ForeignKey(Room, verbose_name=_('Room'), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, verbose_name=_('Movie'), on_delete=models.CASCADE)
    date = models.DateField(verbose_name=_('Release Date'), db_index=True)
    start_at = models.TimeField(verbose_name=_('Release Start At'), db_index=True)
    end_at = models.TimeField(verbose_name=_('Release End At'), db_index=True)

    def __str__(self):
        return f'Release with ID: {self.id}'

    def clean(self):
        if not self.start_at < self.end_at:
            raise ValidationError('The end time must be after the start time')

        # TODO (ehsan) check below code still work?
        time_overlap_condition = Movie.objects.filter(date=self.date).filter(
            Q(start_at__lte=self.start_at, end_at__gte=self.start_at)
            | Q(start_at__lte=self.end_at, end_at__gte=self.end_at)
            | Q(start_at__gte=self.start_at, end_at__lte=self.end_at),
        )
        if self.id:
            time_overlap_condition.exclude(id=self.id)

        if time_overlap_condition.exists():
            raise ValidationError('Another release is available at this time range')

    class Meta:
        verbose_name = _('Release')
        verbose_name_plural = _('Releases')


class Reserve(BaseModel):
    seat = models.ForeignKey(Seat, related_name='reserves', verbose_name=_('Seat'), on_delete=models.CASCADE)
    release = models.ForeignKey(Release, related_name='reserves', verbose_name=_('Release'), on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reserves', verbose_name=_('User'), on_delete=models.CASCADE)

    def __str__(self):
        return f'Reserve with ID: {self.id}'

    class Meta:
        unique_together = ('seat', 'release', 'user')
        verbose_name = _('Reserve')
        verbose_name_plural = _('Reserves')
