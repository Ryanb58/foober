from django.db import models

from django_countries.fields import CountryField


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    location = models.ForeignKey('Location')
    available_timestamp = models.DateTimeField()

    def __str__(self):
        return self.address


class FoodClaim(models.Model):
    food_item = models.ForeignKey('FoodItem', null=False)
    device_uuid = models.UUIDField()
    claim_timestamp = models.DateTimeField(null=False)

    def __str__(self):
        return '{} {}'.format(self.device_uuid)


class Location(models.Model):
    vendor = models.ForeignKey('vendor.Vendor', null=False)
    phone_number = models.CharField(max_length=12)
    phone_extension = models.CharField(max_length=8)
    address = models.CharField(max_length=512)
    city = models.CharField(max_length=512)
    state = models.CharField(max_length=512)
    country = CountryField(blank_label='(select country)')
    longitude = models.CharField(max_length=64)
    latitude = models.CharField(max_length=64)

    def __str__(self):
        return self.address
