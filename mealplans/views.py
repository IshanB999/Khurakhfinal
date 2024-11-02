from django.shortcuts import render,HttpResponse
from django.template import loader
# Create your views here.



def index(request):
    template = loader.get_template('home.html')

    return HttpResponse(template.render())



def signup(request):
    tempate = loader.get_template('auth/signup.html')

    return HttpResponse(tempate.render())

    