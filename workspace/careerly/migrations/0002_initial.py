# Generated by Django 4.1.2 on 2022-11-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('careerly', '0001_careerly'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=120)),
                ('company', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('jobType', models.CharField(max_length=120)),
                ('datePosted', models.DateField()),
                ('posting', models.TextField()),
                ('logoimg', models.ImageField(default=False, upload_to='')),
            ],
        ),
    ]