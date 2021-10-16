from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Tu Nombre', max_length=150, blank= False, null= False)
    apellidos = models.CharField(max_length=200, blank= False, null = False)
    nacionalidad = models.CharField(max_length=150, blank= False, null = False)
    correo = models.EmailField()
    descripcion = models.TextField(blank= False, null = False)
    fecha_creacion = models.DateField('fecha modificacion', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Libro (models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank= False, null = False)
    fecha_publicacion = models.DateField('fecha de publicacion', blank= False, null = False)
    autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE)
    fecha_creacion = models.DateField('fecha modificacion', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'
        ordering = ['titulo']

    def __str__ (self):
        return self.titulo