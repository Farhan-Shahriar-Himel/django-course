from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'author': "Abdur-Rahim", 'age': 5, 'lst': ['1', '2', '3'], 'birth': datetime.datetime.now(), 'courses': [
        {
            "id": 1,
            "name": "python",
            "fee": 1500
        },
        {
            "id": 2,
            "name": 'django',
            "fee": 2000 
        },
        {
            "id": 3,
            "name": 'C-lang',
            "fee": 1000 
        }
    ]}
    return render(request, 'first_app/home.html', d)
