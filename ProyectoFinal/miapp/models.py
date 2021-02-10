from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.CharField(max_length=15, verbose_name="Código")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    hora = models.CharField(max_length=10, verbose_name="Hora")
    creditos = models.CharField(max_length=10, verbose_name="Créditos")
    estado = models.CharField(max_length=1, verbose_name="Estado")
    # auto_now_add=True me pertmite 
    # registrar la fecha de creación del registro
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    # auto_now=True me permite registrar
    # la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Editado")
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['nombre']
    
    
    
    

