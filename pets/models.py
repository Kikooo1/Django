from django.db import models

from django.db import models

class Species(models.Model):
    specie_id = models.AutoField(primary_key=True)
    species_name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Vaccine(models.Model):
    vaccine_id = models.AutoField(primary_key=True)
    vaccine_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PetInfo(models.Model):
    pet_id = models.AutoField(primary_key=True)
    specie = models.ForeignKey(Species, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=60)
    img = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def histories(self):
        return self.history_set.all()

    def vaccines_administered(self):
        return self.vaccinesadministered_set.all()

class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(PetInfo, on_delete=models.CASCADE)
    weight_kg = models.FloatField()
    date_visited = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ReasonOfVisit(models.Model):
    reason_of_visit_id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=100)
    history = models.OneToOneField(History, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VaccinesAdministered(models.Model):
    vaccines_administered_id = models.AutoField(primary_key=True)
    pet = models.ForeignKey(PetInfo, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
