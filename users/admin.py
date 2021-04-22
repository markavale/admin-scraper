from django.contrib import admin
from django.conf import settings
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',  'admin', 'staff', 'active', 'verified']#'ip_address',
    list_filter = ('active','staff','admin', ) # could be date joined
    fieldsets = (
        (None, {'fields': ('username','email', 'password', )}),
        ('Personal info', {'fields': ('verified', 'image', )}),
        ('Permissions', {'fields': ('admin','staff','active',)}),
    )
    # add_fieldsets = UserAdmin.add_fieldsets + (  # For Creating User on Admin Panel
    #     (('Personal Info'), {'fields': ('email','image',)}),#'ip_address',
    # )


admin.site.register(User, UserAdmin)