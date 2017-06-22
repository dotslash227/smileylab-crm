# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from .models import Brand, UserProfile

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "date_added"]
    search_fields = ["name"]

class UserProfileInline(admin.TabularInline):
    model = UserProfile

class UserProfileAdminExtended(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "username", "email", "date_joined", "is_superuser", "is_active"]
    list_display_links = ["username", "first_name", "last_name"]
    search_fields = ["first_name", "last_name", "username", "email"]
    list_filter = ["is_active", "is_staff"]
    list_editable = ["is_active", "is_superuser"]
    inlines = [UserProfileInline]

admin.site.register(Brand, BrandAdmin)
admin.site.unregister(User)
admin.site.register(User, UserProfileAdminExtended)
