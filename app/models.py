# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

class Setting(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    setting_value = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name

class MemberType(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.name

class FileCategory(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.name

class FileRepository(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    fileCategory = models.ForeignKey(FileCategory)
    file_name = models.CharField(max_length=150, blank=True, null=True)
    def __str__(self):
        return self.file_name

class Member(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    memberType = models.ForeignKey(MemberType)
    def __str__(self):
        return self.name

class MemberProperty(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    value = models.CharField(max_length=150, null=True)
    filterValue = models.BooleanField(default=True)
    member = models.ForeignKey(Member)
    possible_values = models.CharField(max_length=150, null=True)
    property_name = models.CharField(max_length=150, blank=True, null=True)
    table_name = models.CharField(max_length=150, blank=True, null=True)
    memberType = models.ForeignKey(MemberType)
    def __str__(self):
        return self.property_name

class Evaluation(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    chart = models.CharField(max_length=150, null=True)
    desc = models.CharField(max_length=150, null=True)
    evalType = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.evalType

class MemberPreference(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    member = models.ForeignKey(Member)
    name = models.CharField(max_length=150, blank=True, null=True)
    value = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name

class Brand(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    member = models.ForeignKey(Member)
    def __str__(self):
        return self.name

class MemberEvaluation(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    evaluation = models.ForeignKey(Evaluation)
    filterValue = models.BooleanField(default=True)
    member = models.ForeignKey(Member)
    pass_values = models.CharField(max_length=150, null=True)
    possible_values = models.CharField(max_length=150, null=True)
    target = models.CharField(max_length=150, null=True)
    tolerance = models.CharField(max_length=150, null=True)


class PatchTolerance(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    active= models.BooleanField(default=True)
    brand = models.ForeignKey(Brand)
    dE2000_level1 = models.FloatField(null=True)
    dE2000_level2 = models.FloatField(null=True)
    dE2000_level3 = models.FloatField(null=True)
    density = models.FloatField(null=True)
    desc = models.CharField(max_length=150, null=True)
    dot_gain = models.FloatField(null=True)
    g7 = models.FloatField(null=True)
    lab_a = models.FloatField(null=True)
    lab_b = models.FloatField(null=True)
    lab_c = models.FloatField(null=True)
    lab_h = models.FloatField(null=True)
    lab_l = models.FloatField(null=True)
    metamerism_level1 = models.FloatField(null=True)
    metamerism_level2 = models.FloatField(null=True)
    metamerism_level3 = models.FloatField(null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    print_contrast = models.FloatField(null=True)
    spectral_1 = models.FloatField(null=True)
    spectral_2 = models.FloatField(null=True)
    spectral_3 = models.FloatField(null=True)
    spectral_4 = models.FloatField(null=True)
    spectral_5 = models.FloatField(null=True)
    spectral_6 = models.FloatField(null=True)
    spectral_7 = models.FloatField(null=True)
    spectral_8 = models.FloatField(null=True)
    spectral_9 = models.FloatField(null=True)
    spectral_10 = models.FloatField(null=True)
    spectral_11 = models.FloatField(null=True)
    spectral_12 = models.FloatField(null=True)
    spectral_13 = models.FloatField(null=True)
    spectral_14 = models.FloatField(null=True)
    spectral_15 = models.FloatField(null=True)
    spectral_16 = models.FloatField(null=True)
    spectral_17 = models.FloatField(null=True)
    spectral_18 = models.FloatField(null=True)
    spectral_19 = models.FloatField(null=True)
    spectral_20 = models.FloatField(null=True)
    spectral_21 = models.FloatField(null=True)
    spectral_22 = models.FloatField(null=True)
    spectral_23 = models.FloatField(null=True)
    spectral_24 = models.FloatField(null=True)
    spectral_25 = models.FloatField(null=True)
    spectral_26 = models.FloatField(null=True)
    spectral_27 = models.FloatField(null=True)
    spectral_28 = models.FloatField(null=True)
    spectral_29 = models.FloatField(null=True)
    spectral_30 = models.FloatField(null=True)
    spectral_31 = models.FloatField(null=True)
    spectral_32 = models.FloatField(null=True)
    spectral_33 = models.FloatField(null=True)
    spectral_34 = models.FloatField(null=True)
    spectral_35 = models.FloatField(null=True)
    spectral_36 = models.FloatField(null=True)
    trap = models.FloatField(null=True)
    version = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name

class Standard(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    icc = models.CharField(max_length=150, null=True)
    version = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    brand = models.ForeignKey(Brand)
    def __str__(self):
        return self.name

class Division(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=150, null=True)
    state =  models.CharField(max_length=150, null=True)
    country = CountryField(null=True)
    member = models.ForeignKey(Member)
    zipCode = models.IntegerField(
                                    validators=[
                                        MinValueValidator(100000),
                                        MaxValueValidator(999999)
                                    ],
                                    null=True
                                )
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    user = models.OneToOneField(User)
    country = CountryField(blank=True, null=True)
    brand = models.ForeignKey(Brand)
    def __str__(self):
        return self.user + "'s profile'"

class PatchStandard(models.Model):
    active= models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)
    brand = models.ForeignKey(Brand)
    density = models.FloatField(null=True)
    dot_gain = models.FloatField(null=True)
    g7 = models.FloatField(null=True)
    geometry = models.CharField(max_length=150, null=True)
    illuminant =  models.CharField(max_length=150, null=True)
    lab_a = models.FloatField(null=True)
    lab_b = models.FloatField(null=True)
    lab_c = models.FloatField(null=True)
    lab_h = models.FloatField(null=True)
    lab_l = models.FloatField(null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    patch = models.CharField(max_length=150, null=True)
    print_contrast = models.FloatField(null=True)
    rgb_b = models.IntegerField(null=True)
    rgb_g = models.IntegerField(null=True)
    rgb_r = models.IntegerField(null=True)
    spectral_1 = models.FloatField(null=True)
    spectral_2 = models.FloatField(null=True)
    spectral_3 = models.FloatField(null=True)
    spectral_4 = models.FloatField(null=True)
    spectral_5 = models.FloatField(null=True)
    spectral_6 = models.FloatField(null=True)
    spectral_7 = models.FloatField(null=True)
    spectral_8 = models.FloatField(null=True)
    spectral_9 = models.FloatField(null=True)
    spectral_10 = models.FloatField(null=True)
    spectral_11 = models.FloatField(null=True)
    spectral_12 = models.FloatField(null=True)
    spectral_13 = models.FloatField(null=True)
    spectral_14 = models.FloatField(null=True)
    spectral_15 = models.FloatField(null=True)
    spectral_16 = models.FloatField(null=True)
    spectral_17 = models.FloatField(null=True)
    spectral_18 = models.FloatField(null=True)
    spectral_19 = models.FloatField(null=True)
    spectral_20 = models.FloatField(null=True)
    spectral_21 = models.FloatField(null=True)
    spectral_22 = models.FloatField(null=True)
    spectral_23 = models.FloatField(null=True)
    spectral_24 = models.FloatField(null=True)
    spectral_25 = models.FloatField(null=True)
    spectral_26 = models.FloatField(null=True)
    spectral_27 = models.FloatField(null=True)
    spectral_28 = models.FloatField(null=True)
    spectral_29 = models.FloatField(null=True)
    spectral_30 = models.FloatField(null=True)
    spectral_31 = models.FloatField(null=True)
    spectral_32 = models.FloatField(null=True)
    spectral_33 = models.FloatField(null=True)
    spectral_34 = models.FloatField(null=True)
    spectral_35 = models.FloatField(null=True)
    spectral_36 = models.FloatField(null=True)
    spin = models.BooleanField(default=True)
    standard = models.ForeignKey(Standard)
    trap = models.FloatField(null=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    active= models.BooleanField(default=True)
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    standard = models.ForeignKey(Standard, null=True)
    product = models.ForeignKey(Product)
    avg_de2000 = models.FloatField(null=True)
    color_match = models.CharField(max_length=150, null=True)
    die_lines =  models.CharField(max_length=150, null=True)
    division = models.ManyToManyField(Division)
    dna_drawdown_submissions =  models.CharField(max_length=150, null=True)
    event = models.CharField(max_length=150, null=True)
    fansworth_test = models.CharField(max_length=150, null=True)
    instrument_status = models.CharField(max_length=150, null=True)
    job_number = models.CharField(max_length = 150, null=True)
    lot_id = models.CharField(max_length = 150, null=True)
    max_de2000 = models.FloatField(null=True)
    pre_engg_meetings = models.CharField(max_length = 150, null=True)
    press_conditions = models.CharField(max_length = 150, null=True)
    press_schedule = models.CharField(max_length = 150, null=True)
    printing_defects = models.CharField(max_length = 150, null=True)
    registration = models.CharField(max_length = 150, null=True)
    responsiveness = models.CharField(max_length = 150, null=True)
    run = models.CharField(max_length = 150, null=True)
    sku_number = models.CharField(max_length = 150, null=True)
    spc = models.CharField(max_length = 150, null=True)
    version = models.CharField(max_length = 150, null=True)
    viewing_conditions = models.CharField(max_length = 150, null=True)
    def __str__(self):
        return self.name

class Device(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    division = models.ForeignKey(Division)
    divisionType = models.CharField(max_length=150, null=True)
    make = models.CharField(max_length=150, null=True)
    model = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name

class UserDivision(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey(User)
    division = models.ForeignKey(Division)
    def __str__(self):
        return self.name

class UserPreference(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150, blank=True, null=True)
    user = models.ForeignKey(User)
    value = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name

class JobPatch(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    job = models.ForeignKey(Job)
    patch_standard=models.ForeignKey(PatchStandard, null=True)
    patch_tolerance=models.ForeignKey(PatchTolerance, null=True)

class Sheet(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    avg_de2000 = models.FloatField(null=True)
    avg_delab = models.FloatField(null=True)
    controlbar_zone = models.CharField(max_length=150, null=True)
    device = models.ForeignKey(Device)
    ink_vendor_c = models.CharField(max_length=150, null=True)
    ink_vendor_k = models.CharField(max_length=150, null=True)
    ink_vendor_m = models.CharField(max_length=150, null=True)
    ink_vendor_y = models.CharField(max_length=150, null=True)
    inkset_c = models.CharField(max_length=150, null=True)
    inkset_k = models.CharField(max_length=150, null=True)
    inkset_m = models.CharField(max_length=150, null=True)
    inkset_y = models.CharField(max_length=150, null=True)
    job = models.ForeignKey(Job)
    max_de2000 = models.FloatField(null=True)
    max_delab = models.FloatField(null=True)
    operator = models.CharField(max_length=150, null=True)
    plate = models.CharField(max_length=150, null=True)
    plate_curve = models.CharField(max_length=150, null=True)
    printing_process = models.CharField(max_length=150, null=True)
    printing_type = models.CharField(max_length=150, null=True)
    sheet_num = models.IntegerField(null=True)
    sheet_side = models.CharField(max_length=150, null=True)
    sheet_type = models.CharField(max_length=150, null=True)
    shift = models.CharField(max_length=150, null=True)
    spectro = models.CharField(max_length=150, null=True)
    spectro_serialnum = models.CharField(max_length=150, null=True)
    substrate = models.CharField(max_length=150, null=True)
    user_id = models.ForeignKey(User)

class Reading(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    de2000  = models.FloatField(null=True)
    density  = models.FloatField(null=True)
    dot_gain  = models.FloatField(null=True)
    g7  = models.FloatField(null=True)
    geometry  = models.CharField(max_length=150, null=True)
    illuminant = models.CharField(max_length=150, null=True)
    job_patch = models.ForeignKey(JobPatch)
    lab_a  = models.FloatField(null=True)
    lab_b  = models.FloatField(null=True)
    lab_c  = models.FloatField(null=True)
    lab_h  = models.FloatField(null=True)
    lab_l  = models.FloatField(null=True)
    metamerism_d50_a  = models.FloatField(null=True)
    metamerism_d50_c  = models.FloatField(null=True)
    metamerism_d50_f11  = models.FloatField(null=True)
    print_contrast  = models.FloatField(null=True)
    rgb_b = models.IntegerField(null=True)
    rgb_g = models.IntegerField(null=True)
    rgb_r = models.IntegerField(null=True)
    sheet_id = models.ForeignKey(Sheet)
    spectral_1 = models.FloatField(null=True)
    spectral_2 = models.FloatField(null=True)
    spectral_3 = models.FloatField(null=True)
    spectral_4 = models.FloatField(null=True)
    spectral_5 = models.FloatField(null=True)
    spectral_6 = models.FloatField(null=True)
    spectral_7 = models.FloatField(null=True)
    spectral_8 = models.FloatField(null=True)
    spectral_9 = models.FloatField(null=True)
    spectral_10 = models.FloatField(null=True)
    spectral_11 = models.FloatField(null=True)
    spectral_12 = models.FloatField(null=True)
    spectral_13 = models.FloatField(null=True)
    spectral_14 = models.FloatField(null=True)
    spectral_15 = models.FloatField(null=True)
    spectral_16 = models.FloatField(null=True)
    spectral_17 = models.FloatField(null=True)
    spectral_18 = models.FloatField(null=True)
    spectral_19 = models.FloatField(null=True)
    spectral_20 = models.FloatField(null=True)
    spectral_21 = models.FloatField(null=True)
    spectral_22 = models.FloatField(null=True)
    spectral_23 = models.FloatField(null=True)
    spectral_24 = models.FloatField(null=True)
    spectral_25 = models.FloatField(null=True)
    spectral_26 = models.FloatField(null=True)
    spectral_27 = models.FloatField(null=True)
    spectral_28 = models.FloatField(null=True)
    spectral_29 = models.FloatField(null=True)
    spectral_30 = models.FloatField(null=True)
    spectral_31 = models.FloatField(null=True)
    spectral_32 = models.FloatField(null=True)
    spectral_33 = models.FloatField(null=True)
    spectral_34 = models.FloatField(null=True)
    spectral_35 = models.FloatField(null=True)
    spectral_36 = models.FloatField(null=True)
    spin = models.BooleanField(default=True)
    trap  = models.FloatField(null=True)

class SheetEvaluation(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    memberEvaluation = models.ForeignKey(MemberEvaluation)
    passname = models.CharField(max_length=150, blank=True, null=True)
    sheet = models.ForeignKey(Sheet)
    value = models.CharField(max_length=150, null=True)
