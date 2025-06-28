from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     path("__reload__/", include("django_browser_reload.urls")),
     path('',include("Projects.urls",namespace="projects")),
    path('blog/',include('blog.urls'))
     
] 

# Configuración para servir archivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # En producción, también servimos archivos media
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



