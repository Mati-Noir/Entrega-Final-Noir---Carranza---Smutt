from django.contrib import admin
from django.urls import path, include
from mi_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
  
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)