from django import forms
from django.db.models import Q
from django.utils import timezone

from .models import Reserve, Release


class ReserveForm(forms.Form):
    release_id = forms.UUIDField()
    seat_id = forms.UUIDField()

    def clean(self):
        cleaned_data = super().clean()

        # TODO (ehsan) run validation

        return cleaned_data
