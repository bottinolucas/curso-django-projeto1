from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("UMA STRING!")

def sobre(request):
    return HttpResponse("Sobre mim!")

def contato(request):
    return HttpResponse("Contato")