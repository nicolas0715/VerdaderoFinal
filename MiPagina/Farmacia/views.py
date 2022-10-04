from django.forms import PasswordInput
from django.shortcuts import render
from Farmacia.models import *
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import logout, authenticate, update_session_auth_hash
from django.contrib.auth import login as login1
from Farmacia.forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#from Farmacia.forms import form_medicamento

# Create your views here.

@login_required
def medicamentos(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    if request.method == "POST":
        medic = Medicamento(
            nombreMarca= request.POST["nombreMarca"],
            drogaComponente= request.POST["drogaComponente"], 
            laboratorio= request.POST["laboratorio"],  
            codigoBarra= request.POST["codigoBarra"]
            )
        medic.save()
        return render(request, "inicio.html", {"avatar": avatar})
    return render(request, "medicamentos.html", {"avatar": avatar}) 

@login_required
def laboratorios(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    if request.method == "POST":
        lab = Laboratorio(
            nombrelab= request.POST["nombreLab"],
            direccionlab= request.POST["direccionLab"], 
            telefonolab= request.POST["telefonoLab"],  
            )
        lab.save()
        return render(request, "laboratorios.html", {"avatar": avatar})
    return render(request, "laboratorios.html", {"avatar": avatar}) 

@login_required
def sucursales(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    if request.method == "POST":
        sucursal = Sucursal(
            nombreSucursal = request.POST["nombreSucursal"],
            direccionSucursal = request.POST["direccionSucursal"], 
            municipioSucursal = request.POST["municipioSucursal"],  
            ciudadSucursal = request.POST["ciudadSucursal"],
            telefonoSucursal = request.POST["telefonoSucursal"],
            )
        sucursal.save()
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None
        return render(request, "sucursales.html", {"avatar": avatar})
    return render(request, "sucursales.html", {"avatar": avatar}) 

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
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "inicio.html", {"avatar": avatar})



def landingpage(request):
    return render(request, "landingpage.html")


@login_required
def ofertas(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "ofertas.html", {"avatar": avatar})


def login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get("username")
            pdw = form.cleaned_data.get("password")
            
            user = authenticate(username = user, password = pdw)

            if user is not None:
                login1(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, "inicio.html", {"avatar": avatar})
            else:
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
#           username = form.cleaned_data["username"]
            form.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "login.html", {"avatar": avatar})
    form = UserRegisterForm()
    return render(request, "signup.html", {"form": form})

@login_required
def editarperfil(request): 
    avatar = Avatar.objects.filter(user = request.user.id)
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get("username")
            user_basic_info.email = form.cleaned_data.get("email")
            user_basic_info.first_name = form.cleaned_data.get("first_name")
            user_basic_info.last_name = form.cleaned_data.get("last_name")
            user_basic_info.save()
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "inicio.html", {"avatar": avatar})
        else:
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "editarperfil.html", {"form": form, "avatar": avatar})
    else:
        form = UserEditForm(initial = {
            "email": usuario.email, 
            "username": usuario.username,
            "first_name": usuario.first_name, 
            "last_name":usuario.last_name
            }
        )
    return render(request, "editarPerfil.html", {"form": form, "avatar": avatar, "usuario": usuario})


@login_required
def changePass(request):
    usuario = request.user
    if request.method == "POST":
#        form = PasswordChangeForm(data = request.POST, user = usuario)
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "changepass.html", {"avatar": avatar})
    else:
#        form = PasswordChangeForm(request.user)
        form = ChangePasswordForm(user = request.user)
    return render(request, "changePass.html", {"form": form, "usuario": usuario})

@login_required
def perfil(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, "perfil.html", {"avatar": avatar})

@login_required
def agregarAvatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    form = AvatarFormulario(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data["avatar"], id = request.user.id)
            avatar.save()
            return render(request, "perfil.html", {"avatar": avatar})
    return render(request, "agregarAvatar.html", {"avatar": avatar, "form": form})

@login_required
def aboutus(request):
    return render(request, "aboutus.html")