from django import forms

class contactFrom(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()