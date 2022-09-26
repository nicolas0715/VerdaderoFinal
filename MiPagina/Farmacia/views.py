from django.shortcuts import render
from Farmacia.models import *
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as login1
from Farmacia.forms import *

from django.contrib.auth.decorators import login_required

#from Farmacia.forms import form_medicamento

# Create your views here.

@login_required
def laboratorios(request):
    return render(request, "laboratorios.html")

@login_required
def medicamentos(request):
    if request.method == "POST":
        medic = Medicamento(
            nombreMarca= request.POST["nombreMarca"],
            drogaComponente= request.POST["drogaComponente"], 
            laboratorio= request.POST["laboratorio"],  
            codigoBarra= request.POST["codigoBarra"]
            )
        medic.save()
        return render(request, "inicio.html")
    return render(request, "medicamentos.html") 

@login_required
def laboratorios(request):
    if request.method == "POST":
        medic = Laboratorio(
            nombreLab= request.POST["nombreLaboratorio"],
            direccion= request.POST["direccion"], 
            telefonoLab= request.POST["telefono"],  
            )
        medic.save()
        return render(request, "inicio.html")
    return render(request, "laboratorios.html") 

@login_required
def sucursales(request):
    if request.method == "POST":
        medic = Medicamento(
            nombreSucursal = request.POST["nombreSucursal"],
            direccionSucursal = request.POST["direccionSucursal"], 
            municipioSucursal = request.POST["municipioSucursal"],  
            ciudadSucursal = request.POST["ciudadSucursal"],
            telefonoSucursal = request.POST["telefonoSucursal"],
            )
        medic.save()
        return render(request, "inicio.html")
    return render(request, "sucursales.html") 

#def api_medicamento(request):
#    if request.method == "POST":
#        formulario = form_medicamento(request.POST)
#        if formulario.is_valid():
#            informacion = formulario.cleaned_data
#            medic = Medicamento(
#                nombreMarca= informacion["nombreMedicamento"],
#                drogaComponente= informacion["nombreDroga"], 
#                laboratorio= informacion["nombreLaboratorio"],  
#                codigoBarra= informacion["codigoBarra"]
#                )
#            medic.save()
#            return render(request, "api_medicamento.html")
#    else:
#        formulario = form_medicamento()
#    return render(request, "api_medicamento.html", {"formulario": formulario})

@login_required
def buscar_medicamento(request):
    if request.GET["nombreMarca"]:
        nombre = request.GET["nombreMarca"]
        medicamentos= Medicamento.objects.filter(nombreMarca__icontains = nombre )
        return render(request, "medicamentos.html", {"medicamentos": medicamentos})
    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

@login_required
def inicio(request):
    return render(request, "inicio.html")

@login_required
def landingpage(request):
    return render(request, "landingpage.html")

@login_required
def ofertas(request):
    return render(request, "ofertas.html")


def login(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pdw = form.cleaned_data.get("password")
            user = authenticate(username = user, password = pdw)
            if user is not None:
                login1(request, user)
                return render(request, "inicio.html")
            else:
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def signup(request):
    if request.method == "POST":
#       form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "inicio.html")
#   form = UserCreationForm()
    form = UserRegisterForm()
    return render(request, "signup.html", {"form": form})

