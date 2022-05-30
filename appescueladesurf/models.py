from django.db import models

# Create your models here.

class Alumnos(models.Model):
    nombre =models.CharField(max_length = 40)
    apellido =models.CharField(max_length = 40)
    edad = models.IntegerField()
    email = models.EmailField()
    numeroalumno=models.IntegerField()


class Profesores(models.Model):
    nombre =models.CharField(max_length =40)
    apellido =models.CharField(max_length =40)
    email =models.EmailField()


class Tutores(models.Model):
    nombre =models.CharField(max_length = 40)
    apellido =models.CharField(max_length =40)
    email = models.EmailField()
    



    

