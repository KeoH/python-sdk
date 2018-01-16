"""Register module."""
from mdwr.responses import Response
from datetime import datetime
from mdwr.paymethod.storedcard import StoredCard


class Register(Response):
    """Register class."""

    def __init__(self, request, response):
        """Initialize."""
        super().__init__(request, response)
        payload = response['payload']
        self.expired_at = payload.get('expired_at')
        self.card_mask = payload.get('card_mask')
        self.token = payload.get('token')
        self.card = None

        if self.expired_at:
            date = datetime.strptime(payload['expired_at'], '%Y-%m-%d').date()
            self.expired_at = date

        if self.token:
            self.card = StoredCard(self.token)
