"""
URL configuration for simple_blog project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Serve media files (uploaded images) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # Force serving media even if DEBUG = False (Temporary fix for Render free tier)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)