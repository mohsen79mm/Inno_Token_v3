from django.contrib import admin
from .models import Post , post_category
from django.contrib.admin import site

admin.site.register(post_category)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith", "content__contains" )
    list_filter = ["author","status","post_cat"]
    list_display = ('title','author', 'status')
    site.disable_action('delete_selected')

    readonly_fields=['author']
    def save_model(self, request, obj, form, change):
            print(request.user.last_name)
            if '/' in obj.url : 
                return None
            if not obj.author:
                obj.author = request.user.last_name
            return super(PostAdmin, self).save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        if obj.author==request.user.last_name or request.user.is_superuser :
            obj.delete()
        return None 

admin.site.register(Post,PostAdmin)