from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, When, Value, BooleanField, Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .forms import ReserveForm
from .models import Room, Movie, Release, Reserve, Seat


class RoomListView(ListView):
    model = Room
    queryset = Room.objects.all()


class RoomMovieListView(ListView):
    model = Movie

    def get_queryset(self):
        room_id = self.request.resolver_match.kwargs['room_id']

        self.room = get_object_or_404(Room, id=room_id)

        now = timezone.localtime()
        return (
            Movie.objects.filter(rooms=self.room, release__date__gte=now.date())
            .annotate(
                has_available_release=Case(
                    When(release__date__gt=now.date(), then=Value(True)),
                    When(release__date=now.date(), release__start_at__gte=now, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                )
            )
            .distinct('id')
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['room'] = self.room
        return context


class RoomMovieReleaseListView(ListView):
    model = Release

    def get_queryset(self):
        room_id = self.request.resolver_match.kwargs['room_id']
        movie_id = self.request.resolver_match.kwargs['movie_id']

        self.movie = get_object_or_404(Movie, id=movie_id)

        now = timezone.localtime()
        # TODO (ehsan) fix below query
        return Release.objects.filter(room_id=room_id, movie=self.movie, date__gte=now.date()).annotate(
            is_available=Case(
                When(date__gt=now.date(), then=Value(True)),
                When(date=now.date(), start_at__gt=now, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['movie'] = self.movie
        return context


class ReleaseDetailView(LoginRequiredMixin, DetailView):
    model = Release
    pk_url_kwarg = 'release_id'

    def get_queryset(self):
        now = timezone.localtime()
        return Release.objects.filter(Q(date__gt=now.date()) | Q(date=now.date(), start_at__gte=now)).select_related(
            'room', 'movie'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['seats'] = Seat.objects.filter(room=self.object.room,).annotate(
            is_reserved=Case(
                When(reserves__release=self.object, then=Value(True)), default=Value(False), output_field=BooleanField()
            )
        )

        return context

    def post(self, request, release_id, *args, **kwargs):
        seat_id = request.POST['seat_id']
        form = ReserveForm(data={'seat_id': seat_id, 'release_id': release_id})

        if form.is_valid():
            reserve = Reserve()
            reserve.seat_id = seat_id
            reserve.release_id = release_id
            reserve.user = self.request.user
            reserve.save()

        # TODO (ehsan) say why you ignored error handling

        return HttpResponseRedirect(reverse('shop:release-detail', kwargs={'release_id': release_id}))
