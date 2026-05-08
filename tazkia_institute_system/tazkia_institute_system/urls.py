from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('circles/', include('circles.urls')),
    path('attendance/', include('attendance.urls')),
    path('grades/', include('grades.urls')),
    path('behavior/', include('behavior.urls')),
    path('notifications/', include('notifications.urls')),
    path('messages/', include('messages_app.urls')),
    path('reports/', include('reports.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
