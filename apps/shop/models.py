from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, F
from django.utils.translation import gettext_lazy as _

from helpers.models import BaseModel


class Room(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'), unique=True)
    description = models.TextField(verbose_name=_('Description'))

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
    room = models.ForeignKey(Room, related_name='movies', verbose_name=_('Room'), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=_('Title'), db_index=True)
    description = models.TextField(verbose_name=_('Description'))
    poster = models.ImageField(upload_to='shop/movie/posters', verbose_name=_('Poster'))
    release_date = models.DateField(verbose_name=_('Release Date'), db_index=True)
    release_start_at = models.TimeField(verbose_name=_('Release Start At'), db_index=True)
    release_end_at = models.TimeField(verbose_name=_('Release End At'), db_index=True)

    def __str__(self):
        return self.title

    def clean(self):
        if not self.release_start_at < self.release_end_at:
            raise ValidationError('The end time must be after the start time')

        if (
            Movie.objects.exclude(title=self.title)
            .filter(release_date=self.release_date)
            .filter(
                Q(release_start_at__lte=self.release_start_at, release_end_at__gte=self.release_start_at)
                | Q(release_start_at__lte=self.release_end_at, release_end_at__gte=self.release_end_at)
                | Q(release_start_at__gte=self.release_start_at, release_end_at__lte=self.release_end_at),
            )
            .exists()
        ):
            raise ValidationError('Another movie is released at this time range')

    class Meta:
        unique_together = ('room', 'title')
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
