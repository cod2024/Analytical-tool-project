from django.db import models

class Members(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    date_of_registration = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    year_of_birth = models.IntegerField()
    county_of_residence = models.CharField(max_length=100)
    sub_county_of_residence = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class EntrepreneurshipCourse(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    duration = models.CharField(max_length=100)
    completion_status = models.BooleanField()

    def _str_(self):
        return self.name

class DataScienceCourse(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    duration = models.CharField(max_length=100)
    completion_status = models.BooleanField()

    def _str_(self):
        return self.name

class MonetizingArtSeminar(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    duration = models.CharField(max_length=100)
    completion_status = models.BooleanField()

    def _str_(self):
        return self.name
