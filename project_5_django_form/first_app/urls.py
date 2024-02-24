from django.urls import path
from . import views


urlpatterns = [
    path('', views.form, name='dj_form'),
    # path('about/', views.about, name='about'),
]
