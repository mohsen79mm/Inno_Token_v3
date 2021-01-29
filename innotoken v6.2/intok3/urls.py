from django.contrib import admin
from django.urls import path,include
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from Blog.sitemaps import StaticViewSitemap,SnippetSitemap

sitemaps = {'static': StaticViewSitemap, 'snippet': SnippetSitemap}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='home'),
    # path('profile/', include('userprofile.urls')),
    path('Blog/', include('Blog.urls') , name='Blog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('service/',include('service.urls')),
    # path('cart/',include('cart.urls')),
    # path('captcha/', include('captcha.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
