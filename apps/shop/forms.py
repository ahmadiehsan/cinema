from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext as _

from .models import Reserve, Release


class ReserveForm(forms.Form):
    release_id = forms.UUIDField()
    seat_id = forms.UUIDField()

    def clean(self):
        cleaned_data = super().clean()
        release_id = cleaned_data['release_id']
        seat_id = cleaned_data['seat_id']

        now = timezone.localtime()
        release = get_object_or_404(Release, id=release_id)
        if release.date < now.date():
            raise ValidationError(_('This release is over'))

        if release.date == now.date() and release.start_at < now.time():
            raise ValidationError(_('This release is over'))

        if Reserve.objects.filter(release_id=release_id, seat_id=seat_id).exists():
            raise ValidationError(_('This seat has already been reserved'))

        return cleaned_data
