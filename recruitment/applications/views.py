from django.shortcuts import render
from .forms import ApplicationForm
from .models import Application
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
  return HttpResponse("<h1>WTF</h1>")

def success(request):
  return HttpResponse(render(request,"applications/success.html"))

def new (request):
  if request.method =="POST":
    form = ApplicationForm(request.POST)
    application = form.save(commit=False)
    application.save()
    return HttpResponseRedirect('./success')

  else:
    form = ApplicationForm()
    return render(request,'applications/application.html',{"form":form })