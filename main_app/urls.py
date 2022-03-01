from django.contrib import admin
from django.urls import path, include


# TODO (ehsan) update urls
urlpatterns = [
    path('', include('apps.core.urls')),
    path('user/', include('apps.user.urls')),
    path('admin/', admin.site.urls),
]
