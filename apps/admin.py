from django.contrib import admin
from .models import Persona #import modelo persona para la creación de ellas en admin en localhost


admin.site.register(Persona)    #Se agrega un register para el modelo Persona.
# Register your models here.
