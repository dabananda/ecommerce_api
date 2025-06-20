from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', RedirectView.as_view(url='/api/v1/', permanent=False)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/', include('api.urls')),
] + debug_toolbar_urls()
