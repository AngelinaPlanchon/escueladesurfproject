from cgitb import html
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict


from appescueladesurf.models import Alumnos, Profesores, Tutores
from appescueladesurf.forms import AlumnoFormulario


# Create your views here.

def alumnos(request):
    alumnos = Alumnos.objects.all


    context_dict = {
        'alumnos' : alumnos
    }

    return render(
        request=request,
        context=context_dict,
        template_name="appescueladesurf/alumno.html"
    )

def profesores(request):
    profesores = Profesores.objects.all

    context_dict = {
        'profesores': profesores
    }

    return render(

        request=request,
        context=context_dict,
        template_name="appescueladesurf/profesores.html"
    )


def tutores(request):
    tutores = Tutores.objects.all


    context_dict = {
        'tutores': tutores
    }
    
    return render(
        request=request,
        context=context_dict,
        template_name="appescueladesurf/tutores.html"
    )


def inicio(request):
    return render(request, "appescueladesurf/inicio.html")

def alumnoFormulario(request):

    if request.method == "POST" :

        miformulario = AlumnoFormulario(request.POST)

        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data

            alumno = Alumnos(
                nombre=informacion['nombre'], 
                apellido=informacion['apellido'], 
                edad=informacion['edad'], 
                email=informacion['email'], 
                numeroalumno=informacion['numeroalumno']
            )

            alumno.save()

            return render(request, "appescueladesurf/inicio.html")

    else:

        miformulario= AlumnoFormulario()

    return render(request, 'appescueladesurf/alumnoFormulario.html', {"miformulario": miformulario})

      

            

def buscaralumno(request):
    return render(request, "appescueladesurf/buscaralumno.html")



def buscar(request):    
    if request.GET['nombre']:
        search_param = request.GET['nombre']
        alumnos = Alumnos.objects.filter(nombre =search_param)

        return render(
            request,"appescueladesurf/buscar.html",{
            'alumnos': alumnos,
            'nombre':search_param
        }

        )
    else:
        respuesta = 'Datos invalidos'
    return HttpResponse(respuesta)
    





