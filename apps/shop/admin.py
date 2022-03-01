from django.contrib import admin
from django.contrib.admin import register

from helpers.admin import BaseAdmin
from .models import Room, Seat, Movie


class SeatInline(admin.TabularInline):
    model = Seat
    extra = 10
    min_num = 1


@register(Room)
class RoomAdmin(BaseAdmin):
    inlines = (SeatInline,)


@register(Movie)
class MovieAdmin(BaseAdmin):
    list_display = ('title', 'room', 'release_date', 'release_start_at', 'release_end_at')
    raw_id_fields = ('room',)
