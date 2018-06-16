from django.db import models

# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    # logo = models.ImageField(
    #     upload_to='myphoto/%Y/%m/%d/', null=True, max_length=255)
    logo_url = models.URLField(max_length=1028)
