from django.contrib import admin
from django.urls import path, include
from apps.views import inicio, crearPersona, editarPersona, eliminarPersona #se importar los métodos de views.py




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',inicio, name = 'index'),
    path('crear_persona/', crearPersona, name = 'crear_persona'),
    path('editar_persona/<int:id>/', editarPersona, name = 'editar_persona'),
    path('eliminar_persona/<int:id>/', eliminarPersona, name = 'eliminar_persona'),
# para login
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),

]

