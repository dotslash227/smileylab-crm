# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as customer

class Category(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class FileRepository(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category)
    created_by = models.ForeignKey(customer)
    file_obj = models.FileField(upload_to="files-repository")
