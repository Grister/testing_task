from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('comments.urls', namespace='comments')),
    path('', include('users.urls', namespace='users')),
    path('captcha/', include('captcha.urls')),
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
