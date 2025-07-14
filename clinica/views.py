from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Paciente, Medico, Cita
from .serializers import PacienteSerializer, MedicoSerializer, CitaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return HttpResponse("Bienvenido a la página principal de la clínica.")

def categorias(request):
    return HttpResponse("Estas son las categorías disponibles.")

def contact(request, name):
    return HttpResponse(f"Hola {name}, esta es la página de contacto.")

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class CitasPorMedicoAPIView(APIView):
    def get(self, request, medico_id):
        citas = Cita.objects.filter(medico_id=medico_id)
        if not citas.exists():
            return Response({"mensaje": "No se encontraron citas para este médico."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CitaSerializer(citas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)