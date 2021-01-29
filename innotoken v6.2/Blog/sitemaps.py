from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['about']
    def location(self, item):
        return reverse(item)

class SnippetSitemap(Sitemap):
    priority = 0.8
    def items(self):
        return Post.objects.all()
    def lastmod(self, obj):
        return obj.created_on
