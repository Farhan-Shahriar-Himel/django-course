from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("This is our courses")


def about(request):
    return HttpResponse("I am farhan. And that's enough about me.")


def home(request):
    return HttpResponse("This is the first app homepage")
