from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 
                  'street_adress1', 'street_adress2', 
                  'town_or_city', 'postcode', 'country')


def __init__(self, *args, **kwargs):

    """Placeholders and classes, remove auto-genereated labels and set autofocus on first field """
    
    super().__init__(*args, **kwargs)
    placeholders = {
        'full_name': 'Full Name',
        'email': 'Email Adress',
        'phone_number': 'Phone Number',
        'country': 'Country',
        'postcode': 'Postal Code',
        'town_or_city': 'Town or City',
        'street_adress1': 'Street Adress 1',
        'street_adress2': 'Street Adress 2'
    }

    self.fields['full_name'].widget.attrs['autofucus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholder[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].lable = False
