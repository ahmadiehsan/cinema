from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        NON_BINARY = 'N', _('Non-Binary')

    birthdate = models.DateField(_('Birthdate'), null=True)
    gender = models.CharField(_('Gender'), max_length=1, choices=Gender.choices, null=True)


# Make unique user's email
User._meta.get_field('email')._unique = True
