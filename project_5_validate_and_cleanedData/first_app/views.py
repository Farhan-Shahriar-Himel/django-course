from django.shortcuts import render
from . forms import Student
# Create your views here.


def student_form(request):
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = Student()
    return render(request, 'first_app/form.html', {'form': form})
