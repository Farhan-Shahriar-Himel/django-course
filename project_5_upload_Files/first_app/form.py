from django import forms

class contactForm(forms.Form):
    name = forms.CharField()
    file = forms.FileField()