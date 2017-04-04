from django.shortcuts import render
from .forms import ApplicationForm
from .models import Application
from django.http import HttpResponse,HttpResponseRedirect

from django.db.models.signals import post_save
from django.dispatch import receiver



def index(request):
  return HttpResponse(render(request,"applications/home.html"))

def success(request):
  return HttpResponse(render(request,"applications/success.html"))

def new (request):
  if request.method =="POST":
    form = ApplicationForm(request.POST, request.FILES)
    application = form.save(commit=False)
    result=application.save()
    return HttpResponseRedirect('./success')

  else:
    form = ApplicationForm()
    return render(request,'applications/application.html',{"form":form })
