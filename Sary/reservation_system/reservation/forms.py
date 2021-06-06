from django import forms


class SeatsForm(forms.Form):
    Seats = forms.NumberInput()