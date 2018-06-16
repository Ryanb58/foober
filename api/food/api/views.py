"""Food Views."""

from rest_framework import viewsets

from food.models import FoodItem
from food.models import FoodClaim
from food.models import Location

from .serializers import FoodItemSerializer
from .serializers import FoodClaimSerializer
from .serializers import LocationSerializer


class FoodItemViewSet(viewsets.ModelViewSet):
    """Food Item View Set."""

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class FoodClaimViewSet(viewsets.ModelViewSet):
    """Food Claim View Set."""

    queryset = FoodClaim.objects.all()
    serializer_class = FoodClaimSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """Location View Set."""

    queryset = Location.objects.all()
    serializer_class = LocationSerializer
