from django.test import TestCase
from applications.models import Application

class ApplicationTestCase(TestCase):
    def setUp(self):
        Application.objects.create(applicant_name="ahmad ", applicant_gender="male",applicant_nationality="JO",applicant_residency="JO",applicant_major="CS",applicant_school="PSUT",applicant_email="ahmadjd94@gmail.com",applicant_about="hello world")
      

    def test(self):
        ahmad = Application.objects.get(applicant_name="ahmad")
    #failing test 