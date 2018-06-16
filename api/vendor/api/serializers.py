"""Food Serializers."""

from rest_framework import serializers
from vendor.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    """Vendor Serializer."""

    class Meta:
        """Meta Class."""

        model = Vendor
        fields = '__all__'

