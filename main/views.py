from pyexpat.errors import messages
import re
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
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

def StudentList(request):
    allStudent = Student.objects.all()
    num_student_cjepljenih  = Student.objects.filter(student_cijepljen=True).count()
    num_student = Student.objects.count()
    context = {'num_student_cjepljenih' : num_student_cjepljenih,'num_student' : num_student, 'allStudent' : allStudent}
    return render(request, 'main/student_list.html', context = context)

def ZaposlenikList(request):
    allZaposlenik = Zaposlenik.objects.all()
    num_zaposlenik_cjepljenih  = Zaposlenik.objects.filter(zaposlenik_cijepljen=True).count()
    num_zaposlenik = Zaposlenik.objects.count()
    context = {'num_zaposlenik_cjepljenih' : num_zaposlenik_cjepljenih,'num_zaposlenik' : num_zaposlenik, 'allZaposlenik' : allZaposlenik}
    return render(request, 'main/zaposlenik_list.html', context = context)

