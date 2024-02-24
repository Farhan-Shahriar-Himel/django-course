from django.shortcuts import render
from . form import contactForm

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    name = request.POST.get('username')
    email = request.POST.get('email')
    rate = request.POST.get('select')
    return render(request, 'first_app/about.html', {'name': name, 'email': email, 'rate': rate})

def form(request):
    return render(request, 'first_app/form.html')

def django_form(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'first_app/django_form.html', {'form' : form})