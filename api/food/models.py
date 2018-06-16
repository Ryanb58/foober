from django.db import models

from django_countries.fields import CountryField


class FoodItem(models.Model):
    TYPE_DAIRY = 0
    TYPE_FRUIT = 1
    TYPE_GRAIN = 2
    TYPE_PROTEIN = 3
    TYPE_VEGETABLES = 4

    TYPE_CHOICES = {
        TYPE_DAIRY: 'Dairy',
        TYPE_FRUIT: 'Fruit',
        TYPE_GRAIN: 'Grain (cereal) foods',
        TYPE_PROTEIN: 'Lean meats, poultry, fish, eggs, tofu, nuts and seeds',
        TYPE_VEGETABLES: 'Vegetables, legumes and beans',
    }

    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    available_timestamp = models.DateTimeField()
    type = models.SmallIntegerField(null=True, choices=TYPE_CHOICES.items())

    def __str__(self):
        return self.name


class FoodClaim(models.Model):
    food_item = models.ForeignKey(
        'FoodItem', on_delete=models.CASCADE, null=False)
    device_uuid = models.UUIDField()
    claim_timestamp = models.DateTimeField(null=False)

    def __str__(self):
        return '{} {}'.format(self.device_uuid)


class Location(models.Model):
    vendor = models.ForeignKey(
        'vendor.Vendor', on_delete=models.CASCADE, null=False)
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
