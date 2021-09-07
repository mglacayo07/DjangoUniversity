from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    context = {'clase': 'Aprendiendo Django'}
    return render(request, 'student_list.html', context)
