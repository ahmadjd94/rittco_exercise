from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
  """docstring for ClassName"""
  class Meta:
    model=Application
    fields = ['applicant_name', 'applicant_gender',
    # "applicant_birthdate",
    # "applicant_nationality",
    # "applicant_residency",
    # "applicant_major",
    # "applicant_school",
    # "applicant_graduation_date",
    # "applicant_email",
    # "applicant_photo",
    # "applicant_about"
    ]
