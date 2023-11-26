from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import CustomUserCreationForm

def patient_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)  
            user = form.save()
            user.is_patient = True
            user.save()
            login(request, user)
            return render(request, 'patient_dashboard.html', {'user': user})
            # return HttpResponse("hello patient")
    else:
        form = CustomUserCreationForm()
    return render(request, 'patient_signup.html', {'form': form})

def doctor_signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.is_doctor = True
            user.save()
            login(request, user)
            return render(request, 'doctor_dashboard.html', {'user': user})
            # return HttpResponse("hello doctor")

    else:
        form = CustomUserCreationForm()
    return render(request, 'doctor_signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_doctor:
                return render(request, 'doctor_dashboard.html', {'user': user})
            elif user.is_patient:
                return render(request, 'patient_dashboard.html', {'user': user})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login/')
def patient_dashboard(request):
    user = request.user
    return render(request, 'patient_dashboard.html', {'user': user})

@login_required(login_url='/login/')
def doctor_dashboard(request):
    user = request.user
    return render(request, 'doctor_dashboard.html', {'user': user})

def logout(request):
    return redirect('authentication:login')
