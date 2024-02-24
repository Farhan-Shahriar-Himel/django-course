from django.shortcuts import render
from . form import contactFrom
# Create your views here.

def form(request):
    form = contactFrom(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'first_app/form.html', {'form': form})

# def about(request):
#     name = request.POST.get('name')
#     email = request.POST.get('email')
#     return render(request, 'first_app/about.html', {'name': name, 'email': email})