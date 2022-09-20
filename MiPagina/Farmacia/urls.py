from django.contrib import admin
from django.urls import path
from Farmacia.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio ),
    path('medicamentos/', medicamentos ),
    path('laboratorios/', laboratorios ),
    path('sucursales/', sucursales ),
    path('ofertas/', ofertas ),
#   path('api_medicamento/', api_medicamento),
    path('buscar_medicamento/', buscar_medicamento),
]

