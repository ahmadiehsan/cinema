from django.contrib import admin
from django.contrib.admin import register

from helpers.admin import BaseAdmin
from .models import Room, Seat, Movie, Release, Reserve


class SeatInline(admin.TabularInline):
    model = Seat
    extra = 10
    min_num = 1


@register(Room)
class RoomAdmin(BaseAdmin):
    inlines = (SeatInline,)
    list_display = ('name', 'color')


@register(Movie)
class MovieAdmin(BaseAdmin):
    pass


@register(Release)
class ReleaseAdmin(BaseAdmin):
    list_display = ('movie', 'room', 'date', 'start_at', 'end_at')
    raw_id_fields = ('room', 'movie')


@register(Reserve)
class ReserveAdmin(BaseAdmin):
    pass
