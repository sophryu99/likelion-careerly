from django.db import models

# Create your models here.
class Careerly(models.Model):
    jobtitle = models.CharField(max_length=120)
    company = models.TextField()
    # completed = models.BooleanField(default=False)

    def _str_(self):
        return self.jobtitle