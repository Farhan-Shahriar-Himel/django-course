from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='userName')
    email = forms.EmailField(label='userEmail')