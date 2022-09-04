from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def sing_inPage(request):
    context = {}
    return render(request, 'Domasno_5_Dnick/sing_in.html',context)
def sing_upPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, 'Account was created for ' + user)
        return redirect('index')
    context = {'form': form}
    return render(request, 'Domasno_5_Dnick/sing_up.html',context)
def forgotPage(request):
    return render(request, 'Domasno_5_Dnick/forgot.html')
def resetpasswordPage(request):
    return render(request, 'Domasno_5_Dnick/resetpassword.html')
def newpasswordPage(request):
    return render(request, 'Domasno_5_Dnick/newpassword.html')
def landingpagePage(request):
    return render(request, 'Domasno_5_Dnick/landingpage.html')
def profilPage(request):
    return render(request, 'Domasno_5_Dnick/profil.html')
def aboutusPage(request):
    return render(request, 'Domasno_5_Dnick/aboutus.html')
def quizPage(request):
    return render(request, 'Domasno_5_Dnick/quiz.html')
def breakfastPage(request):
    return render(request, 'Domasno_5_Dnick/breakfast.html')
def lunchPage(request):
    return render(request, 'Domasno_5_Dnick/lunch.html')
def dinnerPage(request):
    return render(request, 'Domasno_5_Dnick/dinner.html')
def dessertsPage(request):
    return render(request, 'Domasno_5_Dnick/desserts.html')
def certificatePage(request):
    return render(request, 'Domasno_5_Dnick/certificate.html')
def eggsPage(request):
    return render(request, 'Domasno_5_Dnick/eggsbread.html')
def omlettePage(request):
    return render(request, 'Domasno_5_Dnick/omlette.html')
def wrapPage(request):
    return render(request, 'Domasno_5_Dnick/veggiewrap.html')
def nuttyPage(request):
    return render(request, 'Domasno_5_Dnick/nuttychicken.html')
def steakPage(request):
    return render(request, 'Domasno_5_Dnick/steak.html')
def spaghettiPage(request):
    return render(request, 'Domasno_5_Dnick/spaghetti.html')
def mushroomsPage(request):
    return render(request, 'Domasno_5_Dnick/mushroom.html')
def chiaPage(request):
    return render(request, 'Domasno_5_Dnick/chia.html')
def browniesPage(request):
    return render(request, 'Domasno_5_Dnick/brownies.html')
