
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('apps.member.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('product/', include('apps.product.urls')),
    path('order/', include('apps.order.urls')),
    path('event/', include('apps.banner.urls')),
    path('api/', include('apps.api.urls')),
    path('', include('apps.core.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
