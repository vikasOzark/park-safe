from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'username',
        'address',
        'phone_number',
        'is_email_verified',
        'is_phone_verified',
        'joined_date',
        'last_login',
        'is_admin',
        'is_active',
        'is_staff',
        'is_superuser',
     )
    fields = [
        'full_name',
        'email',
        'username',
        'address',
        'phone_number',
        'uuid',
        'is_email_verified',
        'is_phone_verified',
        'joined_date',
        'last_login',
        'is_admin',
        'is_active',
        # 'is_staff',
        'is_superuser',
     ]
    readonly_fields = ['uuid', 'joined_date', 'last_login']