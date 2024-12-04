from django.contrib import admin
from django.urls import path, re_path
from apps.accounts.urls import urlpatterns as user_urls
from apps.products.urls import urlpatterns as product_urls
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny


#Swagger UI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Cafe Management API Docs",
        default_version="v1",
        description="Swagger UI for Cafe Management APIs",
        contact=openapi.Contact(email="abdusattor.work@gmail.com", phone="+998971991313"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^docs(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^api/docs/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + user_urls + product_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

