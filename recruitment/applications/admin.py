from django.contrib import admin
from django.contrib.admin import AdminSite
import sys
# Register your models here.
from .models  import Application

def make_accepted(modeladmin, request, queryset):
    targets = (queryset.all())
    for target in targets:
      apps=Application.objects.filter(id= target.id)
      for app in apps :
        app.accepted=True
        app.save()
        print(app)
    
make_accepted.short_description = "Mark selected applications as accepted"


def make_rejected(modeladmin, request, queryset):
    targets = (queryset.all())
    for target in targets:
      apps=Application.objects.filter(id= target.id)
      for app in apps :
        app.accepted=False
        app.save()
    
make_rejected.short_description = "Mark selected applications as rejected"


class ApplicationAdmin(admin.ModelAdmin):
  list_display = ["created_date","applicant_name",'applicant_birthdate',"applicant_major",'accepted']
  list_display_links = ["applicant_name"]
  list_filter = ["applicant_major"]
  actions = [make_accepted,make_rejected]
  class Meta : 
    model =Application

admin.site.register(Application,ApplicationAdmin)