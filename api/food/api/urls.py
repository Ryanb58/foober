"""Customer API Urls."""

from config.router import Router

from .views import FoodItemViewSet
from .views import FoodClaimViewSet
from .views import LocationViewSet


# pylint: disable=invalid-name
router = Router(version=1, service_name='food')
router.register(r'item', FoodItemViewSet, base_name='item')
router.register(r'claim', FoodClaimViewSet, base_name='claim')
router.register(r'location', LocationViewSet, base_name='location')
