from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from backend.forms import CustomUserCreationForm, CustomUserChangeForm
from backend.models import CustomUser
from django.utils.html import format_html


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    form = CustomUserChangeForm

    model = CustomUser

    list_display = ('first_name', 'last_name', 'email', 'gender', 'dob',  'image_tag', 'is_staff', 'is_active',)

    list_filter = ('first_name', 'last_name', 'email', 'gender', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'gender', 'dob', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'gender', 'dob', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )

    search_fields = ('email',)

    ordering = ('email',)

    def image_tag(self, obj):
        return format_html('<img src ="{}" width ="150" height="150" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


admin.site.register(CustomUser, CustomUserAdmin)