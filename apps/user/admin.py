from django.contrib.admin import register
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext as _

User = get_user_model()


@register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((_('Additional Data'), {'fields': ('birthdate', 'gender')}),)
