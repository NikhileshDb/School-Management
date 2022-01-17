
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from sms import settings
#Token Auth SimpleJwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


#API Docs
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('mainapp.Frontend.frontEndUrls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='SMSGaria')),
    path('api/', get_schema_view(
        title="SMSGariaAcademy",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
