from django import forms
from django.forms.widgets import DateInput
from .models import Country


class FlightSearchForm(forms.Form):
    departure_country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        label='Origin',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    arrival_country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        label='Destination',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date = forms.DateField(
        label='Date of Flight',
        required=False,
        widget=DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'
            }
        )
    )
