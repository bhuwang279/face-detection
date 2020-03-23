from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .api.urls import urlpatterns as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include((api_urls, "api"), namespace="api")),
]