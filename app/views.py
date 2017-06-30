# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate

def index(request):
    return render(request, "index.html", {})
    # if request.method == "POST":
    #     username = request.POST.get("name")
    #     password = request.POST.get("password")
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         if user.is_active:
    #             login(request, user)
    #             return render(request, "user-index.html", {})
    #         else:
    #             return render(request, "login.html", {
    #             "message":"This account has been blocked. Please contact support@smileycolor.com."
    #             })
    #     else:
    #         return render(request, "login.html", {
    #         "message":"User account does not exist"
    #         })
    # else:
    #     if request.user.is_authenticated:
    #         return render(request, "user-index.html", {})
    #     else:
    #         return render(request, "login.html", {})
