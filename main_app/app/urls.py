
from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('json/', views.simple_upload_json, name="json"),
    path('html/', views.simple_upload_html, name="html"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path("docs/", SpectacularSwaggerView.as_view(
        url_name="schema"
    ),
         name="swagger-ui"),
]
