from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include("django_admin_kubi.urls")),
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('api/v1/', include('order.urls')),
    path('api/v1/', include('event.urls')),
    path('api/v1/', include('portfolio.urls')),
    path('api/v1/', include('personal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
