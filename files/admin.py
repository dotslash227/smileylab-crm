# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, FileRepository

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "date_added"]
    search_fields = ["name"]

class FileRepositoryAdmin(admin.ModelAdmin):
    list_display = ["created_by", "category", "date_added", "file_obj"]
    search_fields = ["created_by__username"]
    list_filter = ["created_by__username"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(FileRepository, FileRepositoryAdmin)
