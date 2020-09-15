from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'', include(router.urls)),
    path('api/core/', include('core.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
