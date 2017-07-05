# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

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

def job(request):
    return render(request, "job.html", {})

def division(request):
    return render(request, "division.html", {})

def standard(request):
    return render(request, "standard.html", {})

def patchStandard(request):
    return render(request, "patchStandard.html",
                    {
                      "range36":xrange(1,37),
                      "labRange":["L", "A", "B", "C", "H"],
                      "rgbRange": ["R", "G", "B"],

                    }
                  )

def patchTolerance(request):
    return render(request, "patchTolerance.html",
                    {
                      "range36":xrange(1,37),
                      "labRange":["L", "A", "B", "C", "H"],
                      "metamerismLevelRange": xrange(1,4),
                      "dE2000LevelRange": xrange(1,4),

                    }
                  )
