# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .models import *
from django_countries import countries
from django.http import JsonResponse


def str_to_bool(s):
    if s == 'False':
        return False
    else:
        return True

def index(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "index.html", {})
            else:
                return render(request, "login.html", {
                "message":"This account has been blocked. Please contact support@smileycolor.com."
                })
        else:
            return render(request, "login.html", {
            "message":"User account does not exist"
            })
    else:
        if request.user.is_authenticated:
            return render(request, "index.html", {})
        else:
            return render(request, "login.html", {})

def divisionFromBrand(request):
    resp_dict = {}
    resp_list=[]

    if request.method == "GET":
        brand = Brand.objects.get(pk=int(request.GET.get("brand")))
        member=brand.member
        divisions = Division.objects.filter(member=member)
        for each in divisions:
            data = {}
            data["id"]=each.id
            data["name"]=each.name
            resp_list.append(data)

        resp_dict["divisions"]=resp_list
        return JsonResponse(resp_dict,safe=False)
    else:
        return JsonResponse({"error":"error"})

def job(request):
    if request.method == "POST":
        brand = Brand.objects.get(pk=int(request.POST.get("brand")))
        division
        job
        active = str_to_bool(request.POST.get("active"))

        # name = request.POST.get("name")
        # address = request.POST.get("address")
        # city = request.POST.get("city")
        # state = request.POST.get("state")
        # country = request.POST.get("country")
        # zipCode = int(request.POST.get("zip"))
        # member = Member.objects.get(pk=int(request.POST.get("member")))
        # job = Job(
        #             brand = brand,
        #             division = division,
        #             job = brand,
        #
        #         )
        # division.save()
        return render(request, "app/job.html", {
            "message":"New Job saved successfully!!!",
            "brands":Brand.objects.all(),
        })
    else:
        return render(request, "app/job.html", {
            "message":"",
            "brands":Brand.objects.all(),
        })

def division(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        zipCode = int(request.POST.get("zip"))
        member = Member.objects.get(pk=int(request.POST.get("member")))
        division = Division(
                        name = name,
                        address = address,
                        city = city,
                        state =  state,
                        country = country,
                        member = member,
                        zipCode = zipCode,
                    )
        division.save()
        return render(request, "app/division.html", {
            "message":"New Division saved successfully!!!",
            "members":Member.objects.all(),
            "countries":list(countries),
        })
    else:
        return render(request, "app/division.html", {
            "message":"",
            "members":Member.objects.all(),
            "countries":list(countries),
        })

def standard(request):
    if request.method == "POST":
        name = request.POST.get("standardName")
        icc = request.POST.get("icc")
        version = request.POST.get("version")
        active = str_to_bool(request.POST.get("active"))
        standard = Standard(
                        active = active,
                        name = name,
                        icc = icc,
                        version = version,
                    )
        standard.save()
        return render(request, "app/standard.html", {
            "message":"New Standard saved successfully!!!",
        })
    else:
        return render(request, "app/standard.html", {
            "message":"",
        })

def patchStandard(request):
    if request.method == "POST":
        active = str_to_bool(request.POST.get("active"))
        version = request.POST.get("version")
        brand = Brand.objects.get(pk=int(request.POST.get("brand")))
        density = request.POST.get("density")
        dot_gain = request.POST.get("dotGain")
        g7 = request.POST.get("G7")
        geometry = request.POST.get("geometry")
        illuminant =  request.POST.get("illuminant")
        lab_a = request.POST.get("labA")
        lab_b = request.POST.get("labB")
        lab_c = request.POST.get("labC")
        lab_h = request.POST.get("labH")
        lab_l = request.POST.get("labL")
        name = request.POST.get("name")
        patch = request.POST.get("patch")
        print_contrast = request.POST.get("printContrast")
        rgb_b = request.POST.get("rgbB")
        rgb_g = request.POST.get("rgbG")
        rgb_r = request.POST.get("rgbR")
        spin = request.POST.get("spin")
        standard = Standard.objects.get(pk=int(request.POST.get("standard")))
        trap = str_to_bool(request.POST.get("trap"))

        patchStandard = PatchStandard(
                            active= active,
                            brand = brand,
                            density = density,
                            dot_gain = dot_gain,
                            g7 = g7,
                            geometry = geometry,
                            illuminant =  illuminant,
                            lab_a = lab_a,
                            lab_b = lab_b,
                            lab_c = lab_c,
                            lab_h = lab_h,
                            lab_l = lab_l,
                            name = name,
                            patch = patch,
                            print_contrast = print_contrast,
                            rgb_b = rgb_b,
                            rgb_g = rgb_g,
                            rgb_r = rgb_r,
                            spectral_1 = request.POST.get("spectral1"),
                            spectral_2 = request.POST.get("spectral2"),
                            spectral_3 = request.POST.get("spectral3"),
                            spectral_4 = request.POST.get("spectral4"),
                            spectral_5 = request.POST.get("spectral5"),
                            spectral_6 = request.POST.get("spectral6"),
                            spectral_7 = request.POST.get("spectral7"),
                            spectral_8 = request.POST.get("spectral8"),
                            spectral_9 = request.POST.get("spectral9"),
                            spectral_10 = request.POST.get("spectral10"),
                            spectral_11 = request.POST.get("spectral11"),
                            spectral_12 = request.POST.get("spectral12"),
                            spectral_13 = request.POST.get("spectral13"),
                            spectral_14 = request.POST.get("spectral14"),
                            spectral_15 = request.POST.get("spectral15"),
                            spectral_16 = request.POST.get("spectral16"),
                            spectral_17 = request.POST.get("spectral17"),
                            spectral_18 = request.POST.get("spectral18"),
                            spectral_19 = request.POST.get("spectral19"),
                            spectral_20 = request.POST.get("spectral20"),
                            spectral_21 = request.POST.get("spectral21"),
                            spectral_22 = request.POST.get("spectral22"),
                            spectral_23 = request.POST.get("spectral23"),
                            spectral_24 = request.POST.get("spectral24"),
                            spectral_25 = request.POST.get("spectral25"),
                            spectral_26 = request.POST.get("spectral26"),
                            spectral_27 = request.POST.get("spectral27"),
                            spectral_28 = request.POST.get("spectral28"),
                            spectral_29 = request.POST.get("spectral29"),
                            spectral_30 = request.POST.get("spectral30"),
                            spectral_31 = request.POST.get("spectral31"),
                            spectral_32 = request.POST.get("spectral32"),
                            spectral_33 = request.POST.get("spectral33"),
                            spectral_34 = request.POST.get("spectral34"),
                            spectral_35 = request.POST.get("spectral35"),
                            spectral_36 = request.POST.get("spectral36"),
                            spin = spin,
                            standard = standard,
                            trap =trap,
                        )
        patchStandard.save()
        return render(request, "app/patchStandard.html", {
            "message":"New Brand Color saved successfully!!!",
            "brands" :Brand.objects.all(),
            "standards": Standard.objects.all(),
            "range36":xrange(1,37),
            "labRange":["L", "A", "B", "C", "H"],
            "rgbRange": ["R", "G", "B"],

        })
    else:
        return render(request, "app/patchStandard.html", {
            "message":"",
            "brands" :Brand.objects.all(),
            "standards": Standard.objects.all(),
            "range36":xrange(1,37),
            "labRange":["L", "A", "B", "C", "H"],
            "rgbRange": ["R", "G", "B"],
        })


def patchTolerance(request):
    return render(request, "app/patchTolerance.html",
    {
      "range36":xrange(1,37),
      "labRange":["L", "A", "B", "C", "H"],
      "metamerismLevelRange": xrange(1,4),
      "dE2000LevelRange": xrange(1,4),

    })

def role(request):
    return render(request, "app/role.html", {})

def bookmark(request):
    return render(request, "app/bookmark.html", {})

def link(request):
    return render(request, "app/link.html", {})
