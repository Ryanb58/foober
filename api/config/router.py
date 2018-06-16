"""API Router."""

from rest_framework.routers import DefaultRouter


class Router(DefaultRouter):
    """App Router."""

    def __init__(self, *args, **kwargs):
        """Init."""
        self.version = kwargs.pop('version', 0)
        self.service_name = kwargs.pop('service_name', None)
        super(Router, self).__init__(*args, **kwargs)

    def register(self, prefix, viewset, base_name=None):
        """Register."""
        appname = self.__module__.split('.')[0]

        if self.service_name:
            appname = self.service_name

        prefix = appname + "/v" + str(self.version) + "/" + prefix
        super().register(prefix, viewset, base_name=base_name)
