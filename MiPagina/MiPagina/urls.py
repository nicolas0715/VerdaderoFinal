"""MiPagina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiPagina.view import *
from Farmacia.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingpage ), 
    path('medicamentos/', medicamentos ),
    path('laboratorios/', laboratorios ),
    path('sucursales/', sucursales ),
    path("ofertas/", ofertas),
#   path("api_medicamento/", api_medicamento),
    path("buscar_medicamento/", buscar_medicamento),
    path('buscar_laboratorio/', buscar_laboratorio),
    path('signup/', signup),
    path('login/', login),
    path("inicio/", inicio),
    path("perfil/editarperfil/", editarperfil),
    path("perfil/changepass/", changePass),
    path("perfil/", perfil),
    path("perfil/changeavatar/", agregarAvatar),
    path("aboutus/", aboutus),
    path("loadingTemplate/", loadingTemplate),
    path('logout/', LogoutView.as_view (template_name = "landingpage.html") , name = "Logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)