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
from rest_framework import viewsets
from main.serializers import *
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="accounts/login/")
def StudentList(request):
    allStudent = Student.objects.all()
    num_student_cjepljenih  = Student.objects.filter(student_cijepljen=True).count()
    num_student = Student.objects.count()
    context = {'num_student_cjepljenih' : num_student_cjepljenih,'num_student' : num_student, 'allStudent' : allStudent}
    return render(request, 'main/student_list.html', context = context)

@login_required(login_url="accounts/login/")
def ZaposlenikList(request):
    allZaposlenik = Zaposlenik.objects.all()
    num_zaposlenik_cjepljenih  = Zaposlenik.objects.filter(zaposlenik_cijepljen=True).count()
    num_zaposlenik = Zaposlenik.objects.count()
    context = {'num_zaposlenik_cjepljenih' : num_zaposlenik_cjepljenih,'num_zaposlenik' : num_zaposlenik, 'allZaposlenik' : allZaposlenik}
    return render(request, 'main/zaposlenik_list.html', context = context)

class FakultetStudentList(ListView):

    template_name = 'main/fakultetstudent.html'

    def get_queryset(self):
        self.fakultet = get_object_or_404(Fakultet, fakultet_naziv=self.kwargs['fakultet'])
        return Student.objects.filter(student_fakultet=self.fakultet)

class FakultetViewSet(viewsets.ModelViewSet):
    queryset = Fakultet.objects.all().order_by('fakultet_naziv')
    serializer_class = FakultetSerializer

class CjepivoViewSet(viewsets.ModelViewSet):
    queryset = Cjepivo.objects.all().order_by('cjepivo_naziv')
    serializer_class = CjepivoSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_prezime')
    serializer_class = StudentSerializer

class ZaposlenikViewSet(viewsets.ModelViewSet):
    queryset = Zaposlenik.objects.all().order_by('zaposlenik_prezime')
    serializer_class = ZaposlenikSerializer