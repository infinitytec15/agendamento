from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.users.urls')),
    path('api/', include('apps.clients.urls')),
    path('api/', include('apps.schedules.urls')),
    path('api/', include('apps.notifications.urls')),
    path('api/', include('apps.subscriptions.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
]
