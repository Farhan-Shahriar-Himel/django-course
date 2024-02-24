from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='homepage'),
    path("about/", views.about, name='about'),
    path("form/", views.form, name='form'),
    path("django_form/", views.django_form, name='django_form')
]
