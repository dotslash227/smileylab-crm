# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField

class Brand(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    country = CountryField(blank=True, null=True)
    brand = models.ForeignKey(Brand)

    def __str__(self):
        return self.user + "'s profile'"
