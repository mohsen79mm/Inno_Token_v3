from django.contrib import admin
from .models import Post , post_category

admin.site.register(post_category)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith", "content__contains" )
    list_filter = ["author","status","post_cat"]
    list_display = ('title','author', 'status')

    readonly_fields=['author']
    def save_model(self, request, obj, form, change):
            if '/' in obj.url : 
                return None        
            obj.author = request.user.last_name
            return super(PostAdmin, self).save_model(request, obj, form, change)
    def delete_model(self, request, obj):
        if obj.author==request.user.last_name or "SuperBlog"==request.user.last_name :
            obj.delete()
        return None 

admin.site.register(Post,PostAdmin)