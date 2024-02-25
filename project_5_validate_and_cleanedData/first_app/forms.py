from django import forms
from django.core import validators


# class Student(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     val_name = self.cleaned_data['name']
#     #     if len(val_name) < 10:
#     #         raise forms.ValidationError("Your name must have minimum 10 characters")
#     #     return val_name
    
#     # def clean_email(self):
#     #     val_email = self.cleaned_data['email']
#     #     if 'gmail.com' not in val_email:
#     #         raise forms.ValidationError("Please correct your email")
#     #     return val_email

#     def clean(self):
#         cleaned_data = super().clean()
#         val_name = self.cleaned_data['name']
#         val_email = self.cleaned_data['email']

#         if len(val_name) < 10:
#             raise forms.ValidationError("Your name must have minimum 10 characters")
#         if 'gmail.com' not in val_email:
#             raise forms.ValidationError("Please correct your email")
        

class Student(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='your name must have 10 characters')])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="correct your email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message=["you are not applicable"]), validators.MinValueValidator(24, message=["you are not applicable"])])