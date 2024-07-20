from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Compras(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    size = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nombre


class Visitantes(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email=models.EmailField()

class Profesores(models.Model):
    nombre= models.CharField(max_length=50)
    edad=models.IntegerField()
    horarios=models.IntegerField()
    profesion= models.CharField(max_length=50)



class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
