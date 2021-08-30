from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('django.contrib.flatpages.urls')),
    path('news/', include('django.contrib.flatpages.urls')),
]
