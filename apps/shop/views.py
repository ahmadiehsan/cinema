from django.views.generic import ListView

from .models import Room


class RoomListView(ListView):
    model = Room
    queryset = Room.objects.all()
