from pyexpat.errors import messages
import re
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from main.models import *
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


## Create your views here.
class FakultetList(ListView):
    model = Fakultet

class CjepivoList(ListView):
    model = Cjepivo

class StudentList(ListView):
    model = Student

class ZaposlenikList(ListView):
    model = Zaposlenik

def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('login')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, "Odjavili ste se!")
    return redirect('/')