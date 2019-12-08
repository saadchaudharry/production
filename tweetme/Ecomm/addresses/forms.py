from django import forms
from .models import Address


class Addressform(forms.ModelForm):
    class Meta:
        model = Address
        fields=[
            # "bill",
            # "Address_type",
            "address_1",
            "address_2",
            "country",
            "state",
            "city",
            "pin_code",
            "contact_no"
        ]