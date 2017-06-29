# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

class Setting(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    setting_value = models.CharField(max_length=150)

class MemberType(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class FileCategory(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)

class FileRepository(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    active = models.BooleanField()
    fileCategory = models.ForeignKey(FileCategory)
    file_name = models.CharField(max_length=150)

class MemberProperty(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    value = models.CharField(max_length=150)
    filterValue = models.BooleanField()
    member = models.ForeignKey(Member)
    possible_values = models.CharField(max_length=150)
    property_name = models.CharField(max_length=150)
    table_name = models.CharField(max_length=150)
    memberType = models.ForeignKey(MemberType)

class Member(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    memberType = models.ForeignKey(MemberType)
    def __str__(self):
        return self.name

class Evaluation(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    chart = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)
    evalType = models.CharField(max_length=150)

class MemberPreference(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    member = models.ForeignKey(Member)
    name = models.CharField(max_length=150)
    value = models.CharField(max_length=150)

class Brand(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    member = models.ForeignKey(Member)
    def __str__(self):
        return self.name

class MemberEvaluation(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    evaluation = models.ForeignKey(Evaluation)
    filterValue = models.BooleanField()
    member = models.ForeignKey(Member)
    pass_values = models.CharField(max_length=150)
    possible_values = models.CharField(max_length=150)
    target = models.CharField(max_length=150)
    tolerance = models.CharField(max_length=150)

class PatchTolerance(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    active= models.BooleanField()
    brand = models.ForeignKey(Brand)
    dE2000_level1 = models.FloatField()
    dE2000_level2 = models.FloatField()
    dE2000_level3 = models.FloatField()
    density = models.FloatField()
    desc = models.CharField(max_lenght=150)
    dot_gain = models.FloatField()
    g7 = models.FloatField()
    lab_a = models.FloatField()
    lab_b = models.FloatField()
    lab_c = models.FloatField()
    lab_h = models.FloatField()
    lab_l = models.FloatField()
    metamerism_level1 = models.FloatField()
    metamerism_level2 = models.FloatField()
    metamerism_level3 = models.FloatField()
    name = models.CharField(max_lenght=150)
    print_contrast = models.FloatField()
    spectral_1 = models.FloatField()
    spectral_10 = models.FloatField()
    spectral_11 = models.FloatField()
    spectral_12 = models.FloatField()
    spectral_13 = models.FloatField()
    spectral_14 = models.FloatField()
    spectral_15 = models.FloatField()
    spectral_16 = models.FloatField()
    spectral_17 = models.FloatField()
    spectral_18 = models.FloatField()
    spectral_19 = models.FloatField()
    spectral_2 = models.FloatField()
    spectral_20 = models.FloatField()
    spectral_21 = models.FloatField()
    spectral_22 = models.FloatField()
    spectral_23 = models.FloatField()
    spectral_24 = models.FloatField()
    spectral_25 = models.FloatField()
    spectral_26 = models.FloatField()
    spectral_27 = models.FloatField()
    spectral_28 = models.FloatField()
    spectral_29 = models.FloatField()
    spectral_3 = models.FloatField()
    spectral_30 = models.FloatField()
    spectral_31 = models.FloatField()
    spectral_32 = models.FloatField()
    spectral_33 = models.FloatField()
    spectral_34 = models.FloatField()
    spectral_35 = models.FloatField()
    spectral_36 = models.FloatField()
    spectral_4 = models.FloatField()
    spectral_5 = models.FloatField()
    spectral_6 = models.FloatField()
    spectral_7 = models.FloatField()
    spectral_8 = models.FloatField()
    spectral_9 = models.FloatField()
    trap = models.FloatField()
    version = models.CharField(max_lenght=150)

class Standard(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    icc = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand)
    version = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Product(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand)
    def __str__(self):
        return self.name

class Division(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state =  models.CharField(max_length=150)
    country = CountryField()
    member = models.ForeignKey(Member)
    zipCode = models.IntegerField(
                                    validators=[
                                        MaxValueValidator(000000),
                                        MinValueValidator(999999)
                                    ]
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
    date_added = models.DateTimeField(default=timezone.now)
    brand = models.ForeignKey(Brand)
    date_added = models.DateTimeField(default=timezone.now)
    density = models.FloatField()
    dot_gain = models.FloatField()
    g7 = models.FloatField()
    geometry = models.CharField(max_length=150)
    illuminant models.CharField(max_length=150)
    lab_a = models.FloatField()
    lab_b = models.FloatField()
    lab_c = models.FloatField()
    lab_h = models.FloatField()
    lab_l = models.FloatField()
    name = models.CharField(max_length=150)
    patch = models.CharField(max_length=150)
    print_contrast = models.FloatField()
    rgb_b = models.IntegerField()
    rgb_g = models.IntegerField()
    rgb_r = models.IntegerField()
    spectral_1 = models.FloatField()
    spectral_10 = models.FloatField()
    spectral_11 = models.FloatField()
    spectral_12 = models.FloatField()
    spectral_13 = models.FloatField()
    spectral_14 = models.FloatField()
    spectral_15 = models.FloatField()
    spectral_16 = models.FloatField()
    spectral_17 = models.FloatField()
    spectral_18 = models.FloatField()
    spectral_19 = models.FloatField()
    spectral_2 = models.FloatField()
    spectral_20 = models.FloatField()
    spectral_21 = models.FloatField()
    spectral_22 = models.FloatField()
    spectral_23 = models.FloatField()
    spectral_24 = models.FloatField()
    spectral_25 = models.FloatField()
    spectral_26 = models.FloatField()
    spectral_27 = models.FloatField()
    spectral_28 = models.FloatField()
    spectral_29 = models.FloatField()
    spectral_3 = models.FloatField()
    spectral_30 = models.FloatField()
    spectral_31 = models.FloatField()
    spectral_32 = models.FloatField()
    spectral_33 = models.FloatField()
    spectral_34 = models.FloatField()
    spectral_35 = models.FloatField()
    spectral_36 = models.FloatField()
    spectral_4 = models.FloatField()
    spectral_5 = models.FloatField()
    spectral_6 = models.FloatField()
    spectral_7 = models.FloatField()
    spectral_8 = models.FloatField()
    spectral_9 = models.FloatField()
    spin = models.BooleanField()
    standard = models.ForeignKey(Standard)
    trap = models.FloatField()

class Job(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    standard = models.ForeignKey(Standard)
    product = models.ForeignKey(Product)
    avg_de2000 = models.FloatField()
    color_match = models.CharField(max_length=150)
    die_lines =  models.CharField(max_length=150)
    division = models.ForeignKey(Division)
    dna_drawdown_submissions =  models.CharField(max_length=150)
    event = models.CharField(max_length=150)
    fansworth_test = models.CharField(max_length=150)
    instrument_status = models.CharField(max_length=150)
    job_number = models.CharField(max_length = 150)
    lot_id = models.CharField(max_length = 150)
    max_de2000 = models.FloatField()
    pre_engg_meetings = models.CharField(max_length = 150)
    press_conditions = models.CharField(max_length = 150)
    press_schedule = models.CharField(max_length = 150)
    printing_defects = models.CharField(max_length = 150)
    registration = models.CharField(max_length = 150)
    responsiveness = models.CharField(max_length = 150)
    run = models.CharField(max_length = 150)
    sku_number = models.CharField(max_length = 150)
    spc = models.CharField(max_length = 150)
    version = models.CharField(max_length = 150)
    viewing_conditions = models.CharField(max_length = 150)
    def __str__(self):
        return self.name

class Device(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    division = models.ForeignKey(Division)
    divisionType = models.CharField(max_length=150)
    make = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class UserDivision(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    division = models.ForeignKey(Division)
    def __str__(self):
        return self.name

class UserPreference(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    value = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class JobPatch(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    job = models.ForeignKey(Job)
    patch_standard_id=models.IntegerField()
    patch_tolerance_id=models.IntegerField()

class Sheet(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    avg_de2000 = models.FloatField()
    avg_delab = models.FloatField()
    controlbar_zone = models.CharField(max_length=150)
    device = models.ForeignKey(Device)
    ink_vendor_c = models.CharField(max_length=150)
    ink_vendor_k = models.CharField(max_length=150)
    ink_vendor_m = models.CharField(max_length=150)
    ink_vendor_y = models.CharField(max_length=150)
    inkset_c = models.CharField(max_length=150)
    inkset_k = models.CharField(max_length=150)
    inkset_m = models.CharField(max_length=150)
    inkset_y = models.CharField(max_length=150)
    job = models.ForeignKey(Job)
    max_de2000 = models.FloatField()
    max_delab = models.FloatField()
    operator = models.CharField(max_length=150)
    plate = models.CharField(max_length=150)
    plate_curve = models.CharField(max_length=150)
    printing_process = models.CharField(max_length=150)
    printing_type = models.CharField(max_length=150)
    sheet_num = models.IntegerField()
    sheet_side = models.CharField(max_length=150)
    sheet_type = models.CharField(max_length=150)
    shift = models.CharField(max_length=150)
    spectro = models.CharField(max_length=150)
    spectro_serialnum = models.CharField(max_length=150)
    substrate = models.CharField(max_length=150)
    user_id = models.ForeignKey(User)

class Reading(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    de2000  = models.FloatField()
    density  = models.FloatField()
    dot_gain  = models.FloatField()
    g7  = models.FloatField()
    geometry  = models.CharField(max_length=150)
    illuminant = models.CharField(max_length=150)
    job_patch = models.ForeignKey(JobPatch)
    lab_a  = models.FloatField()
    lab_b  = models.FloatField()
    lab_c  = models.FloatField()
    lab_h  = models.FloatField()
    lab_l  = models.FloatField()
    metamerism_d50_a  = models.FloatField()
    metamerism_d50_c  = models.FloatField()
    metamerism_d50_f11  = models.FloatField()
    print_contrast  = models.FloatField()
    rgb_b = models.IntegerField()
    rgb_g = models.IntegerField()
    rgb_r = models.IntegerField()
    sheet_id = models.ForeignKey(Sheet)
    spectral_1  = models.FloatField()
    spectral_10  = models.FloatField()
    spectral_11  = models.FloatField()
    spectral_12  = models.FloatField()
    spectral_13  = models.FloatField()
    spectral_14  = models.FloatField()
    spectral_15  = models.FloatField()
    spectral_16  = models.FloatField()
    spectral_17  = models.FloatField()
    spectral_18  = models.FloatField()
    spectral_19  = models.FloatField()
    spectral_2  = models.FloatField()
    spectral_20  = models.FloatField()
    spectral_21  = models.FloatField()
    spectral_22  = models.FloatField()
    spectral_23  = models.FloatField()
    spectral_24  = models.FloatField()
    spectral_25  = models.FloatField()
    spectral_26  = models.FloatField()
    spectral_27  = models.FloatField()
    spectral_28  = models.FloatField()
    spectral_29  = models.FloatField()
    spectral_3  = models.FloatField()
    spectral_30  = models.FloatField()
    spectral_31  = models.FloatField()
    spectral_32  = models.FloatField()
    spectral_33  = models.FloatField()
    spectral_34  = models.FloatField()
    spectral_35  = models.FloatField()
    spectral_36  = models.FloatField()
    spectral_4  = models.FloatField()
    spectral_5  = models.FloatField()
    spectral_6  = models.FloatField()
    spectral_7  = models.FloatField()
    spectral_8  = models.FloatField()
    spectral_9  = models.FloatField()
    spin = models.BooleanField()
    trap  = models.FloatField()

class SheetEvaluation(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    memberEvaluation = models.ForeignKey(MemberEvaluation)
    passName = models.CharField(max_length=150)
    sheet = models.ForeignKey(Sheet)
    value = models.CharField(max_length=150)
