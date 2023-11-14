# import djngo
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello this is home page in django")


def about(request):
    return HttpResponse("About Us")