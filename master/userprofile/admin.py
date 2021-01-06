from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import cuser

class CustomerUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = cuser
    list_display = ('user_type', 'phone', 'website', 'is_staff', 'is_active')
    list_filter = ('phone', 'website', 'user_type')

    fieldsets = (
        ('اطلاعات اولیه', {'fields': ('phone','last_name', 'website', 'name_of_company','password')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','last_name' ,  'website', 'name_of_company','user_type', 'password1', 'password2',)}
         ),
    )

    ordering = ('phone',)
admin.site.register(cuser, CustomerUserAdmin)