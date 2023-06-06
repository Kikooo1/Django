from django.forms import ModelForm, ModelChoiceField, Textarea, CharField, DateTimeField, DateTimeInput
from .models import PetInfo, Species, Vaccine, ReasonOfVisit, History, VaccinesAdministered

class SpeciesForm(ModelForm):
    class Meta:
        model = Species
        fields = ['species_name']  # List all the fields you need in the form

class VaccinesForm(ModelForm):
    class Meta:
        model = Vaccine
        fields = ['vaccine_name']  # List all the fields you need in the form


class PetInfoForm(ModelForm):
    specie = ModelChoiceField(queryset=Species.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = PetInfo
        fields = ['pet_id', 'specie', 'pet_name', 'owner_name', 'img']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specie'].queryset = Species.objects.all()

        # Customize the specie field's display text
        self.fields['specie'].label_from_instance = lambda obj: obj.species_name

class ReasonOfVisitForm(ModelForm):
    class Meta:
        model = ReasonOfVisit
        fields = ['reason']


class HistoryForm(ModelForm):
    pet = ModelChoiceField(queryset=PetInfo.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = History
        fields = ['history_id', 'pet', 'weight_kg', 'date_visited']
        widgets = {
            'date_visited': DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pet'].queryset = PetInfo.objects.all()
        self.fields['pet'].label_from_instance = lambda obj: obj.pet_name

class VaccinesAdministeredForm(ModelForm):
    pet = ModelChoiceField(queryset=PetInfo.objects.all(), empty_label="(Nothing)")
    vaccine = ModelChoiceField(queryset=Vaccine.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = VaccinesAdministered
        fields = ['vaccines_administered_id', 'pet', 'vaccine']
