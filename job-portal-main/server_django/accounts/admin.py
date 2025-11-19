from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'fullname', 'role')
    ordering = ('email',)
    search_fields = ('email', 'fullname')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fullname','phoneNumber','role')}),
        ('Profile', {'fields': ('profile_bio','profile_skills','profile_resume')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','fullname','phoneNumber','role','password1','password2')
        }),
    )

admin.site.register(User, UserAdmin)
