from django.db import models

# Create your models here.

# Data Model for Job Postings
class JobPosting(models.Model):
    jobtitle = models.CharField(max_length=120)
    company = models.TextField()
    # completed = models.BooleanField(default=False)

    def _str_(self):
        return self.jobtitle