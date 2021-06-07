from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def home(request):
    return render(request,'user/home.html')

def register(request):
    if request.method=='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quizoption')
    else:
        form=UserRegisterForm()
    return render(request,'user/register.html', {'form': form})


def quizoption(request):
    return render(request,'user/quizoption.html')
