from django import forms

class contactForm(forms.Form):
    name = forms.CharField()
    file = forms.FileField(required=False)
    meal = [('p', 'papperoni'), ('m', 'mashroom'), ('B', 'beef')]
    pizza = forms.MultipleChoiceField(choices=meal, widget= forms.CheckboxSelectMultiple)
    birthday = forms.CharField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))