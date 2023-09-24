from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from families.views import FamilyViewSet
from users.views import WTSUserViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="WTS Backend Main API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

router = routers.DefaultRouter()
router.register(r'api/v1/users', WTSUserViewSet, basename='users')
router.register(r'api/v1/families', FamilyViewSet, basename='families')

urlpatterns += router.urls
