from django.shortcuts import render
from .forms import ApplicationForm
from .models import Application
# Create your views here.

from django.http import HttpResponse

def index(request):
  return HttpResponse("<h1>WTF</h1>")
def new (request):
  if request.method =="POST":
    form = ApplicationForm(request.POST)
    application = form.save(commit=False)
    application.save()
  else:
    form = ApplicationForm()
    return render(request,'applications/application.html',{"form":form })