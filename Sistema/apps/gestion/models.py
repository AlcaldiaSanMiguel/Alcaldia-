from __future__ import unicode_literals
from __future__ import absolute_import
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.db import models

# Create your models here.
class ContenidoPrograma(models.Model):
	nombre_contenido = models.CharField(max_length=40)
	imagen_contenido = models.ImageField(upload_to='programas/')
	class Meta:
		verbose_name='Contenido programa'
		verbose_name_plural='Contenido Galeria Programas'
	def __str__(self):
		return '%s' %(self.nombre_contenido)

@receiver(post_delete, sender=ContenidoPrograma)
def imagenes_programas_delete(sender, instance, **kwargs):
	instance.imagen_contenido.delete(False)

class ContenidoProyecto(models.Model):
	nombre_Contproyecto = models.CharField(max_length=40)
	imagen_Contproyecto = models.ImageField(upload_to='proyectos/')
	class Meta:
		verbose_name='Contenido  proyectos'
		verbose_name_plural='Contenidos Galeria Proyectos'
	def __str__(self):
		return '%s' %(self.nombre_Contproyecto)

@receiver(post_delete, sender=ContenidoProyecto)
def imagenes_programas_delete(sender, instance, **kwargs):
	instance.imagen_Contproyectodelete(False)



class ContenidoGaleriaTurismo(models.Model):
	nombre_foto = models.CharField(max_length=100)
	imagen_galeria = models.ImageField(upload_to='turismoFotos/')

	class Meta:
		verbose_name = 'Contenido Turismo'
		verbose_name_plural = 'Contenido Galeria Turismo'
	def __str__(self):
		return '%s' %(self.nombre_foto)

@receiver(post_delete, sender=ContenidoGaleriaTurismo)
def imagen_galeria(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen_galeria.delete(False)

class ContenidoGaleriaComida(models.Model):
    nombre_foto = models.CharField(max_length=100)
    imagen_galeria = models.ImageField(upload_to='comidaFotos/')

    class Meta:
        verbose_name = 'Contenido Comida'
        verbose_name_plural = 'Contenido Galeria Comida'
    def __str__(self):
        return '%s' %(self.nombre_foto)

@receiver(post_delete, sender=ContenidoGaleriaComida)
def imagen_galeria(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen_galeria.delete(False)

class ContenidoGaleriaFestival(models.Model):
    nombre_foto = models.CharField(max_length=100)
    imagen_galeria = models.ImageField(upload_to='festivalFotos/')

    class Meta:
        verbose_name = 'Contenido Festival'
        verbose_name_plural = 'Contenido Galeria Festival'
    def __str__(self):
        return '%s' %(self.nombre_foto)

@receiver(post_delete, sender=ContenidoGaleriaFestival)
def imagen_galeria(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen_galeria.delete(False)

class ContenidoGaleriaFiesta(models.Model):
    nombre_foto = models.CharField(max_length=100)
    imagen_galeria = models.ImageField(upload_to='fiestaFotos/')

    class Meta:
        verbose_name = 'Contenido Fiesta'
        verbose_name_plural = 'Contenido Galeria Fiesta'
    def __str__(self):
        return '%s' %(self.nombre_foto)

@receiver(post_delete, sender=ContenidoGaleriaFiesta)
def imagen_galeria(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen_galeria.delete(False)