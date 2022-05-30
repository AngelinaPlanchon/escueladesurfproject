from django.urls import path
from appescueladesurf import views

urlpatterns = [
    path('alumno/',views.alumnos, name='Alumno'),
    path('profesores/',views.profesores, name='Profesores'),
    path('tutores/',views.tutores, name='Tutores'),
    path('',views.inicio, name='Inicio'),
    path('alumnoFormulario/', views.alumnoFormulario, name='alumnoFormulario'),
    path('buscaralumno/', views.buscaralumno, name='buscaralumno'),
   path('buscar/', views.buscar, name = 'Buscar')






]