from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from django.views.generic import TemplateView

from tools.views import MaterialViewSet, MaterialTypeViewSet, EntityViewSet, EntityTypeViewSet, UserTypeViewSet, UserViewSet, UserMaterialViewSet
from rest_framework.schemas import get_schema_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.SimpleRouter()
router.register('material', MaterialViewSet, basename='material')
router.register('materialtype', MaterialTypeViewSet, basename='materialtype')
router.register('entity', EntityViewSet, basename='entity')
router.register('entitytype', EntityTypeViewSet, basename='entitytype')
router.register('material', MaterialViewSet, basename='material')
router.register('user', UserViewSet, basename='user')
router.register('usertype', UserTypeViewSet, basename='usertype')
router.register('request', UserMaterialViewSet, basename='request')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('openapi/', get_schema_view(
        title="ODC Tools Manager",
        description="The management of tools in ODC"
    ), name='openapi-schema'),

    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # allauth
    path('accounts/', include('allauth.urls')),


    path('api/', include(router.urls))
]
