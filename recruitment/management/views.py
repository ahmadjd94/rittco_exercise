from django.shortcuts import render
from applications.models import Application
from django.http import HttpResponse,HttpResponseRedirect
from django.forms.models import model_to_dict
def index(request):
  all_responses=Application.objects.all()
  return HttpResponse(render(request,"management/index.html",{'all_responses':all_responses}))

