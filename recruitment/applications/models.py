from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField

# Create your models here.

class Application(models.Model):
    #ID field is not specified since it's a default
    
    created_date = models.DateTimeField(
            default=timezone.now)
    applicant_name = models.TextField()
    applicant_gender = models.CharField(max_length = 6)
    applicant_birthdate = models.DateField(null = True)
    applicant_nationality = CountryField(null =True,blank_label= ("(SELECT NATIONALITY)"))
    applicant_residency = CountryField(null =True,blank_label= ("(SELECT RESIDNECY)"))
    applicant_major = models.TextField(null = True)
    applicant_school = models.TextField(null = True)
    applicant_graduation_date = models.DateField(null = True)
    applicant_email = models.EmailField(null = True)
    applicant_photo = models.ImageField(null = True)
    applicant_about = models.TextField(max_length = 500,null = True)


    def __str__(self):
        return self.applicant_name


