from django.shortcuts import render

# Create your views here.
# home/views.py

def home(request):
    return render(request, 'home/index.html')