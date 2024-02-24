from django import forms

class contactFrom(forms.Form):
    # name = forms.CharField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # appointment = forms.DateTimeField()
    size = forms.ChoiceField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')])
    pizza = forms.MultipleChoiceField(choices=[('p', 'papperoni'), ('m', 'mashroom'), ('b', 'beef')])