from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sanem(request):
    return HttpResponse('<h1>Dear Mahadeva after talking with u i feel calm</h1>')
def mahadev(request):
    return HttpResponse('<h1><i>I feel happy thalli i also love you as kannayya did ,dont worry about anything</i></h1>')
