from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from main import urls as  main_app_urls
from Users import urls as users_app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_app_urls)),
    path('', include(users_app_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)