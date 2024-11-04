from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from django.contrib.auth.models import User
from .models import (
    Customer,
)
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
import json
from django.http import JsonResponse

# Create your views here.



def index(request):
    user = request.user

    context = {
        'user':request.user
    }
    return render(request,'home.html',context=context)



def signup(request):

    if request.user.is_authenticated:
        return redirect('/')  # Replace 'home' with the appropriate URL name or pat


    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create the User
        user = User.objects.create_user(
            username=email,  # or generate a unique username from email or another field
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Create the Customer
        customer = Customer.objects.create(user=user)
        
        # Log the user in and redirect to a success or home page
        login(request, user)
        return redirect('/')  # Replace 'home' with your actual redirect URL
    
    return render(request, 'auth/signup.html')


def login_view(request):

    
    if request.user.is_authenticated:
        return redirect('/')  # Replace 'home' with the appropriate URL name or pat

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('/')  # Change to your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'home.html')  # Redirect to base template to render popup





def logout_view(request):
    logout(request)
    return redirect('/')  # Change 'home' to your desired redirect URL after logout


def bmi_calculator(request):
    template = loader.get_template('bmi/calculator.html')


    return HttpResponse(template.render())

    
