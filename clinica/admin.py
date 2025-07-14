from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Paciente, Medico, Cita, Especialidad

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cita)
admin.site.register(Especialidad)
