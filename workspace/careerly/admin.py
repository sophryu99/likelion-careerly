from django.contrib import admin

from .models import JobPosting

class CareerlyAdmin(admin.ModelAdmin):
    list_display = ('jobtitle', 'company')


# Register your models here.
admin.site.register(JobPosting, CareerlyAdmin)