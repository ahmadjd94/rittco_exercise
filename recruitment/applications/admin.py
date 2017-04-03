from django.contrib import admin
from django.contrib.admin import AdminSite
import sys
# Register your models here.
from .models  import Application
from .models  import Admin_Application

def make_accepted(modeladmin, request, queryset):
    targets = (queryset.all())
    for target in targets:
      print(Admin_Application.objects.filter(application_id= target.id))
    # map (lambda target :Admin_Application.)
    # queryset.update(status='p')
make_accepted.short_description = "Mark selected applications as accepted"

class ApplicationAdmin(admin.ModelAdmin):
  list_display = ["created_date","applicant_name",'applicant_birthdate',"applicant_major"]
  list_display_links = ["applicant_name"]
  list_filter = ["applicant_major"]
  actions = [make_accepted]
  class Meta : 
    model =Application

admin.site.register(Application,ApplicationAdmin)