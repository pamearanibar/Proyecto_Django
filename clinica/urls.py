from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from .views import CitasPorMedicoAPIView 

# Router de la API REST
router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet)
router.register(r'medicos', views.MedicoViewSet)
router.register(r'citas', views.CitaViewSet)

urlpatterns = [
    # Rutas normales (vistas con HttpResponse)
    path('', views.index, name='index'),
    path('categorias/', views.categorias, name='categorias'),
    path('contact/<str:name>/', views.contact, name='contacto'),

    # Rutas para la API REST
    path('', include(router.urls)),

    path('citas/medico/<int:medico_id>/', CitasPorMedicoAPIView.as_view(), name='citas-por-medico'),
]
