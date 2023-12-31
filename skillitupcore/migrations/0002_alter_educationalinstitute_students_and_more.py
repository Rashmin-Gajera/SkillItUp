# Generated by Django 4.1 on 2022-08-10 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skillitupcore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalinstitute',
            name='students',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='educationalinstitute',
            name='subdomains',
            field=models.ManyToManyField(blank=True, to='skillitupcore.subdomain'),
        ),
    ]
