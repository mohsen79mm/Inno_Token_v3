from django.contrib import admin
from django.urls import path,include
from .views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    path('profile/', include('userprofile.urls')),
    path('Blog/', include('Blog.urls') , name='Blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include('service.urls')),
    path('cart/',include('cart.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
