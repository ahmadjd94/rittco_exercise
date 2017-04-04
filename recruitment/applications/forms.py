from django import forms
from .models import Application
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from datetime import datetime
class ApplicationForm(forms.ModelForm):
  """docstring for ClassName"""
  genders=[('Male', 'male'), ('Female', 'female')]
  applicant_gender  = forms.ChoiceField( widget=forms.RadioSelect(),choices= genders)
  applicant_birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1920,datetime.today().year-18)))
  widgets={'applicant_residency':CountrySelectWidget(),
  'applicant_nationality':CountrySelectWidget()}
  applicant_graduation_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1985, datetime.today().year+10)))

  class Meta:
    model=Application
    fields = ['applicant_name', 'applicant_gender',
     "applicant_birthdate",
     "applicant_nationality",
    "applicant_residency",
    "applicant_major",
    "applicant_school",
    "applicant_graduation_date",
    "applicant_email",
     "applicant_photo",  #use AWS ? 
    "applicant_about"
    ]
