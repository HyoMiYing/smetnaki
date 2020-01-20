# Django imports
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
# Project imports
from .models import Koncert
from datetimewidget.widgets import DateTimeWidget

class AddKoncertForm(forms.ModelForm):
    class Meta:
        model = Koncert
        fields = (
            'concert_date_time',
            'concert_venue',
            'concert_ticket_price',
            )
        labels = {
            'concert_date_time' : _('Date and time:'),
            'concert_venue' : _('Venue:'),
            'concert_ticket_price' : _('Ticket price:'),
            }

