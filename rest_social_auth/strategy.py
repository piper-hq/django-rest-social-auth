import contextlib
from social_django.strategy import DjangoStrategy


class DRFStrategy(DjangoStrategy):

    def __init__(self, storage, request=None, tpl=None):
        self.request = request
        self.session = {}

        if request:
            with contextlib.suppress(AttributeError):
                self.session = request.session
        super().__init__(storage, tpl)

    def request_data(self, merge=True):
        if self.request:
            return getattr(self.request, 'auth_data', {})
        else:
            return {}
