
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

...
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...


if settings.DEBUG:
    schema_view = get_schema_view(
            openapi.Info(
               title="Pizza Delivery API",
               description="Pizza Delivery service",
               default_version="1.0",
               contact=openapi.Contact(email="admin@app.com"),
               license=openapi.License(name="BSD License"),
            ),
            public=True,
            permission_classes=(permissions.AllowAny,),
        )
else:
    schema_view = get_schema_view(
        openapi.Info(
            title="Global plug",
            description="A travel agency",
            default_version="1.0",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        url="https://web-pizza-delivery.up.railway.app/swagger/"
    )

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('auth/', include('authentication.urls')),
   path('orders/', include('orders.urls')),
   path('auth/', include('djoser.urls.jwt')),
]


