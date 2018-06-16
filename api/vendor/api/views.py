"""Food Views."""

from rest_framework import viewsets

from vendor.models import Vendor

from .serializers import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """Food Item View Set."""

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
