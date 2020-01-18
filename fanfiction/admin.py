from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from fanfics.models import Fanfic

UserAdmin.fieldsets += (None, {'fields': ('is_dark',)}),

admin.site.register(User, UserAdmin)
admin.site.register(Fanfic)