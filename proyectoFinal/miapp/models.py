from django.db import models

# Create your models here.

#Modelo usuario
class Usuario(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('user', 'Usuario'),
        ('grupo', 'Grupo'),
        ('sala', 'Sala'),
    ]
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(max_length=10, choices=ROLES)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    id_usuario = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    dni= models.CharField(max_length=9, unique=True, blank=True, null=True)
    cif= models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nombre, self.email
