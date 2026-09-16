from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to home page or any other page
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Create your views here.
