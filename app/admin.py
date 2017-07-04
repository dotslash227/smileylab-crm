# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

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

admin.site.register(Setting)
admin.site.register(MemberType)
admin.site.register(FileCategory)
admin.site.register(FileRepository)
admin.site.register(Member)
admin.site.register(MemberProperty)
admin.site.register(Evaluation)
admin.site.register(MemberPreference)
#   admin.site.register(Brand)
admin.site.register(MemberEvaluation)
admin.site.register(PatchTolerance)
admin.site.register(Standard)
admin.site.register(Product)
admin.site.register(Division)
#admin.site.register(UserProfile)
admin.site.register(PatchStandard)
admin.site.register(Job)
admin.site.register(Device)
admin.site.register(UserDivision)
admin.site.register(UserPreference)
admin.site.register(JobPatch)
admin.site.register(Sheet)
admin.site.register(Reading)
admin.site.register(SheetEvaluation)
