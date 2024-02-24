from django.shortcuts import render
from . form import contactForm

# Create your views here.
def form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            file = form.cleaned_data['file']
            with open('first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return render(request, 'first_app/form.html', {'form': form})
    else:
        form = contactForm()

    return render(request, 'first_app/form.html', {'form': form})