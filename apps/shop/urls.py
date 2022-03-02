from django.urls import path

from .views import RoomListView, RoomMovieListView, RoomMovieReleaseListView, ReleaseDetailView

app_name = 'shop'

urlpatterns = [
    path('', RoomListView.as_view(), name='room-list'),
    path('rooms/<uuid:room_id>/movies/', RoomMovieListView.as_view(), name='room-movie-list'),
    path(
        'rooms/<uuid:room_id>/movies/<uuid:movie_id>/releases/',
        RoomMovieReleaseListView.as_view(),
        name='room-movie-release-list',
    ),
    path('releases/<uuid:release_id>/', ReleaseDetailView.as_view(), name='release-detail'),
]
