from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key= True) #Campo autoincrementador, clave primaria.
    nombre = models.CharField(max_length= 100 ) #tipo caracter
    apellido = models.CharField(max_length= 120) #tipo caracter
    correo = models.EmailField(max_length= 200)

    def __str__(self):
        return self.nombre