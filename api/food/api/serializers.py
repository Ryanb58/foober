"""Food Serializers."""

from rest_framework import serializers
from food.models import FoodItem
from food.models import FoodClaim
from food.models import Location


class FoodItemSerializer(serializers.ModelSerializer):
    """FoodItem Serializer."""

    class Meta:
        """Meta Class."""

        model = FoodItem
        fields = '__all__'


class FoodClaimSerializer(serializers.ModelSerializer):
    """FoodItem Serializer."""

    class Meta:
        """Meta Class."""

        model = FoodClaim
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    """FoodItem Serializer."""

    class Meta:
        """Meta Class."""

        model = Location
        fields = '__all__'
