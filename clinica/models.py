from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def validar_ci(value):
    if not value.isdigit() or len(value) < 5:
        raise ValidationError("El CI debe contener al menos 5 dígitos numéricos.")


def validar_fecha_nacimiento(value):
    fecha_actual = timezone.localtime().date()  
    if value > fecha_actual:
        raise ValidationError("La fecha de nacimiento no puede ser futura.")

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    registro_medico = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Dr(a). {self.nombre}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    ci = models.CharField(max_length=15, unique=True, validators=[validar_ci])
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])

    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)


class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"{self.fecha} - {self.paciente.nombre} con {self.medico.nombre}"
