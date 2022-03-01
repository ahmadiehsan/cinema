from django.urls import path

from .views import RoomListView

app_name = 'shop'

urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
]
