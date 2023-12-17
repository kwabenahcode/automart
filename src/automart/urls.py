from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from main import urls as main_view_urls

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_view_urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)