from django.db import models
from django.utils import timezone
# Create your models here.

class Application(models.Model):
    #ID field is not specified since it's a default
    
    created_date = models.DateTimeField(
            default=timezone.now)
    applicant_name = models.TextField()
    applicant_gender = models.CharField(max_length = 6)
    applicant_birthdate = models.DateField()
    applicant_nationality = models.TextField()
    applicant_residency = models.TextField()
    applicant_major = models.TextField()
    applicant_school = models.TextField()
    applicant_graduation_date = models.DateField()
    applicant_email = models.EmailField()
    applicant_photo = models.ImageField()
    applicant_about = models.TextField(max_length = 500)


    def __str__(self):
        return self.applicant_name


