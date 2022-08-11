from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from accounts.forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required


def home(request):
    if not request.user.is_authenticated:
        posts=Blog.objects.all()
    else:
        posts=Blog.objects.filter(user=request.user)
    fields=CategoryTree.objects.all()
    if request.user.is_authenticated:
        info=Individual_info()
        info=Individual_info.objects.filter(user=request.user)
        return render(request, 'artistapp/index.html',{'fields':fields,'posts':posts,'info':info})
    else:
        return render(request, 'artistapp/index.html',{'fields':fields,'posts':posts,})


def dongmoon(request):
    return render(request, 'artistapp/dongmoon.html')
