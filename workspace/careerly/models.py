from django.db import models

# Create your models here.

# Data Model for Job Postings
class JobPosting(models.Model):
    jobtitle = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    jobType = models.CharField(max_length=120)
    datePosted = models.DateField()
    posting = models.TextField()
    logoimg = models.ImageField(default = False)

    def _str_(self):
        return self.jobtitle