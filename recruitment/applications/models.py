from django.db import models
from django.utils import timezone
# Create your models here.

class Application(models.Model):
    #ID field is not specified since it's a default
    
    created_date = models.DateTimeField(
            default=timezone.now)
    applicant_name = models.TextField()
    applicant_gender = models.CharField(max_length = 6)
    applicant_birthdate = models.DateField(null = True)
    applicant_nationality = models.TextField(null = True)
    applicant_residency = models.TextField(null = True)
    applicant_major = models.TextField(null = True)
    applicant_school = models.TextField(null = True)
    applicant_graduation_date = models.DateField(null = True)
    applicant_email = models.EmailField(null = True)
    applicant_photo = models.ImageField(null = True)
    applicant_about = models.TextField(max_length = 500,null = True)


    def __str__(self):
        return self.applicant_name


