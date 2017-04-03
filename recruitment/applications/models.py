from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save

# Create your models here.

class Admin_Application(models.Model):
    application = models.ForeignKey("Application",null =True,unique= True)
    admin =models.ForeignKey(User,null =True)
    accepted =models.NullBooleanField(null =True)

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
    applicant_photo = models.ImageField(null = True,upload_to ='avatars')
    applicant_about = models.TextField(max_length = 500,null = True)


    def __str__(self):
        return self.applicant_name

def create_relation(sender,**kwargs):
    relation =Admin_Application(application_id= kwargs['instance'].id)
    relation.save()

post_save.connect(create_relation,sender=Application)
    
        


