from django.contrib import admin
from django.urls import path
from Farmacia.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', landingpage),
    path('medicamentos/', medicamentos ),
    path('laboratorios/', laboratorios ),
    path('sucursales/', sucursales ),
    path('ofertas/', ofertas ),
#   path('api_medicamento/', api_medicamento),
    path('buscar_medicamento/', buscar_medicamento),
    path('signup/', signup),
    path('login/', login),
    path('logout/', LogoutView.as_view (template_name = "landingpage.html") , name = "Logout"),
]

