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
        active

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
        Active = request.POST.get("active")
        standard = Standard(
                        active = str_to_bool(Active),
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
    return render(request, "app/patchStandard.html",
                    {
                      "range36":xrange(1,37),
                      "labRange":["L", "A", "B", "C", "H"],
                      "rgbRange": ["R", "G", "B"],

                    }
                  )

def patchTolerance(request):
    return render(request, "app/patchTolerance.html",
                    {
                      "range36":xrange(1,37),
                      "labRange":["L", "A", "B", "C", "H"],
                      "metamerismLevelRange": xrange(1,4),
                      "dE2000LevelRange": xrange(1,4),

                    }
                  )

def role(request):
    return render(request, "app/role.html", {})

def bookmark(request):
    return render(request, "app/bookmark.html", {})

def link(request):
    return render(request, "app/link.html", {})
