from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.urls import path
from .models import Species, Vaccine, PetInfo, VaccinesAdministered, History
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PetInfoForm, SpeciesForm, VaccinesForm, HistoryForm, ReasonOfVisitForm, VaccinesAdministeredForm


def pets(request):
    return render(request, 'pets/pets.html')

def createPet(request):
    form = PetInfoForm()

    if request.method == 'POST':
        form = PetInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Pet created')

    context = {'form': form}
    return render(request, 'pets/pet_form.html', context)



# CRUD for Species
def species_list(request):
    species = Species.objects.all()
    return render(request, 'species_list.html', {'species': species})

def species_create(request):
    if request.method == "POST":
        form = SpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('species_list')
    else:
        form = SpeciesForm()
    return render(request, 'species_form.html', {'form': form})

def species_update(request, pk):
    species = get_object_or_404(Species, pk=pk)
    if request.method == "POST":
        form = SpeciesForm(request.POST, instance=species)
        if form.is_valid():
            form.save()
            return redirect('species_list')
    else:
        form = SpeciesForm(instance=species)
    return render(request, 'species_form.html', {'form': form})

def species_delete(request, pk):
    species = get_object_or_404(Species, pk=pk)
    if request.method == "POST":
        species.delete()
        return redirect('species_list')
    return render(request, 'species_confirm_delete.html', {'object': species})


# views.py
def vaccines_list(request):
    vaccines = Vaccine.objects.all()
    return render(request, 'vaccines_list.html', {'vaccines': vaccines})

def vaccines_create(request):
    if request.method == "POST":
        form = VaccinesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vaccines_list')
    else:
        form = VaccinesForm()
    return render(request, 'vaccines_form.html', {'form': form})

def vaccines_update(request, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    if request.method == "POST":
        form = VaccinesForm(request.POST, instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('vaccines_list')
    else:
        form = VaccinesForm(instance=vaccine)
    return render(request, 'vaccines_form.html', {'form': form})

def vaccines_delete(request, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    if request.method == "POST":
        vaccine.delete()
        return redirect('vaccines_list')
    return render(request, 'vaccines_confirm_delete.html', {'object': vaccine})



def pet_info_list(request):
    pets = PetInfo.objects.all()
    return render(request, 'pet_info_list.html', {'pets': pets})

def pet_info_create(request):
    if request.method == "POST":
        form = PetInfoForm(request.POST, request.FILES)  # request.FILES is show the uploaded image
        if form.is_valid():
            form.save()
            return redirect('pet_info_list')
    else:
        form = PetInfoForm()
    return render(request, 'pet_info_form.html', {'form': form})

def pet_info_update(request, pk):
    pet = get_object_or_404(PetInfo, pk=pk)
    if request.method == "POST":
        form = PetInfoForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_info_list')
    else:
        form = PetInfoForm(instance=pet)
    return render(request, 'pet_info_form.html', {'form': form})

def pet_info_delete(request, pk):
    pet = get_object_or_404(PetInfo, pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('pet_info_list')
    return render(request, 'pet_info_confirm_delete.html', {'object': pet})


# views.py
def history_create(request, pk):
    pet = get_object_or_404(PetInfo, pk=pk)

    if request.method == "POST":
        form = HistoryForm(request.POST)
        reason_form = ReasonOfVisitForm(request.POST)

        if form.is_valid() and reason_form.is_valid():
            history = form.save(commit=False)
            history.pet = pet
            history.save()

            reason = reason_form.save(commit=False)
            reason.history = history
            reason.save()

            return redirect('pet_info_list')  # Replace with the appropriate URL name or path

    else:
        history_form = HistoryForm(initial={'pet': pet})
        reason_form = ReasonOfVisitForm()

    return render(request, 'history_form.html', {'form': history_form, 'reason_form': reason_form})

def vaccines_administered_create(request, pk):
    pet = get_object_or_404(PetInfo, pk=pk)
    if request.method == "POST":
        form = VaccinesAdministeredForm(request.POST)
        if form.is_valid():
            vaccines_administered = form.save(commit=False)
            vaccines_administered.pet = pet  # assign the pet to the vaccines_administered
            vaccines_administered.save()
            return redirect('pet_info_list')
    else:
        form = VaccinesAdministeredForm(initial={'pet': pet})  # initialize pet field with specific pet
    return render(request, 'vaccines_administered_form.html', {'form': form})


def pet_info_detail(request, pk):
    pet = get_object_or_404(PetInfo, pk=pk)
    histories = History.objects.filter(pet_id=pk)
    vaccines_administered = VaccinesAdministered.objects.filter(pet_id=pk)
    return render(request, 'pet_info_detail.html', {'pet': pet, 'histories': histories, 'vaccines_administered': vaccines_administered})