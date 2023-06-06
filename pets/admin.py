from django.contrib import admin

# Register your models here.
from .models import PetInfo, Species, Vaccine, History, ReasonOfVisit, VaccinesAdministered

admin.site.register(PetInfo)
admin.site.register(Species)
admin.site.register(Vaccine)
admin.site.register(History)
admin.site.register(ReasonOfVisit)
admin.site.register(VaccinesAdministered)
