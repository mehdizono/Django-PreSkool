from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    return render(request, 'Home/index.html') 

# Add this new function to fix the crash
def index(request):
    return HttpResponse("Welcome to the School App!")