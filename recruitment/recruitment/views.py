from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import admin


def home(request):
  return HttpResponse(render(request,"recruitment/home.html"))

