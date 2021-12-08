from django.shortcuts import render
from django.http import HttpResponse

## Create your views here.
def homepage(request):
    return HttpResponse('Welcome to COVID app. <br> Made by Marko, Matej and Dominik!')
    # primjetiti korištenje HTML-a