"""Customer API Urls."""

from config.router import Router

from .views import VendorViewSet


# pylint: disable=invalid-name
router = Router(version=1, service_name='vendor')
router.register(r'vendor', VendorViewSet, base_name='vendor')
