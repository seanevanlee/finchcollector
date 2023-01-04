from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch, Wing
from .forms import FeedingForm

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

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


def home(request):
    # return HttpResponse('<h1>It is finching time!</h1>')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    wings_finch_doesnt_have = Wing.objects.exclude(
        id__in=finch.wings.all().values_list('id'))
    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form, 'wings': wings_finch_doesnt_have})


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'color', 'description', 'age']
    success_url = '/finches/'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


class WingList(ListView):
    model = Wing


class WingDetail(DetailView):
    model = Wing


class WingCreate(CreateView):
    model = Wing
    fields = ['name', 'color']


class WingUpdate(UpdateView):
    model = Wing
    fields = ['name', 'color']


class WingDelete(DeleteView):
    model = Wing
    success_url = '/wings/'


def assoc_wing(request, finch_id, wing_id):
    Finch.objects.get(id=finch_id).wings.add(finch_id)
    return redirect('detail', finch_id=finch_id)
