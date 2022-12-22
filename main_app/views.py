from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

from .models import Finch
# Define the home view


# class Finch:
#     def __init__(self, name, breed, sound, age):
#         self.name = name
#         self.breed = breed
#         self.sound = sound
#         self.age = age


# This the array, we are injecting into the template
# finches = [
#     Finch('Geospiza magnirostris', 'brown', 'chirp chirp', 1),
#     Finch('Geospiza fortis', 'gray', 'chirp chirp', 2),
#     Finch('Geospiza fuliginosa', 'spotted gray', 'chirp chirp', 3)
# ]


def home(request):
    return HttpResponse('<h1>It is finching time!</h1>')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})
