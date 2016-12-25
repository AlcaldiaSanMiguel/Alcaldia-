from __future__ import unicode_literals
from __future__ import absolute_import
from django.db.models.signals import post_delete
from django.dispatch import receiver

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from django.db import models

from apps.gestion.models import *

# Create your models here.

class Mensaje(models.Model):
	nombre = models.CharField(max_length=30)
	email  = models.CharField(max_length=50)
	mensaje = models.CharField(max_length=500)
	class Meta:
		verbose_name='Mensaje'
		verbose_name_plural='Mensajes'
	def __str__(self):
		return '%s' %(self.nombre)


class ContactosEmergencia(models.Model):
	nombre_contacto = models.CharField(max_length=30)
	telefono=models.CharField(max_length=9)
	class Meta:
		verbose_name='Contacto de emergencia'
		verbose_name_plural='Contactos de emergencia'
	def __str__(self):
		return '%s' %(self.nombre_contacto)


class Noticias(models.Model):
	nombre_noticia = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=2000)
	imagen_descriptiva = models.ImageField(upload_to='noticias/')

	class Meta:
		verbose_name='Noticia'
		verbose_name_plural = 'Noticias'
	def __str__(self):
		return '%s' %(self.nombre_noticia)

@receiver(post_delete, sender=Noticias)
def noticia_delete(sender, instance, **kwargs):
	instance.imagen_descriptiva.delete(False)

class Programa(models.Model):
	nombre_programa = models.CharField(max_length=70, unique=True)
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	imagen  = models.ManyToManyField(ContenidoPrograma)

	class Meta:
		verbose_name='Programa'
		verbose_name_plural='Programas'
	def __str__(self):
		return '%s' %(self.nombre_programa)

class TipoProyecto(models.Model):
	tipo_proyecto = models.CharField(max_length=30)
	class Meta:
		verbose_name='Tipo proyecto'
		verbose_name_plural = 'Tipos proyectos'
	def __str__(self):
		return '%s' %(self.tipo_proyecto)

class Proyecto(models.Model):
	tipo_proyecto = models.OneToOneField(TipoProyecto)
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	imagen  = models.ManyToManyField(ContenidoProyecto)

	class Meta:
		verbose_name='Proyecto'
		verbose_name_plural='Proyectos'
	def __str__(self):
		return '%s' %(self.tipo_proyecto)

class TipoTasa(models.Model):
	nombre_tipo = models.CharField(max_length=30)
	class Meta:
		verbose_name='Tipo tasa municipal'
		verbose_name_plural = 'Tipo tasas municipales'
	def __str__(self):
		return '%s' %(self.nombre_tipo)


class Tasas(models.Model):
	tipo = models.OneToOneField(TipoTasa)
	nombre_tasa = models.CharField(max_length=70)
	monto = models.FloatField()

	class Meta:
		verbose_name='Tasa municipal'
		verbose_name_plural = 'Tasas Municipales'
	def __str__(self):
		return '%s' %(self.nombre_tasa)

class Documento(models.Model):
	nombre_documento = models.CharField(max_length=100)
	archivo = models.FileField(upload_to='documentos/')

	class Meta:
		verbose_name='Documento'
		verbose_name_plural='Documentos'
	def __str__(self):
		return '%s' %(self.nombre_documento)

class Hermanamientos(models.Model):
	descripcion = models.CharField(max_length=500)
	imagen  = models.ManyToManyField(ContenidoPrograma)

	class Meta:
		verbose_name='Hermanamiento'
		verbose_name_plural='Hermanamientos'
	def __str__(self):
		return '%s' %(self.descripcion)


class Historia(models.Model):
	titulo_historia = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=5000)
	imagen_descriptiva = models.ImageField(upload_to='historias/')

	class Meta:
		verbose_name='Historia'
		verbose_name_plural = 'Historias'
	def __str__(self):
		return '%s' %(self.titulo_historia)

@receiver(post_delete, sender=Historia)
def imagen_descriptiva_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen_descriptiva.delete(False)

class Turismo(models.Model):
	nombre= models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	imagen  = models.ImageField(upload_to='turismoTemas/')

	class Meta:
		verbose_name='Turismo'
		verbose_name_plural='Turismos'
	def __str__(self):
		return '%s' %(self.nombre)

@receiver(post_delete, sender=Turismo)
def imagen(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen.delete(False)



class TurismoFotos(models.Model):
	categoria = models.ForeignKey(Turismo)
	nombre_foto = models.CharField(max_length=100)
	imagen_turismo = models.ManyToManyField(ContenidoGaleriaTurismo)
	class Meta:
		verbose_name='Turismo Foto'
		verbose_name_plural='Turismo Fotos'
	def __str__(self):
		return '%s' %(self.nombre_foto)


class Comida(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen  = models.ImageField(upload_to='comidaTemas/')

    class Meta:
        verbose_name='Comida'
        verbose_name_plural='Comidas'
    def __str__(self):
        return '%s' %(self.nombre)

@receiver(post_delete, sender=Comida)
def imagen(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen.delete(False)



class ComidaFotos(models.Model):
    categoria = models.ForeignKey(Comida)
    nombre_foto = models.CharField(max_length=100)
    imagen_comida = models.ManyToManyField(ContenidoGaleriaComida)
    class Meta:
        verbose_name='ComidaFoto'
        verbose_name_plural='Comida Fotos'
    def __str__(self):
        return '%s' %(self.nombre_foto)


class Festival(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    imagen  = models.ImageField(upload_to='festivalTemas/')

    class Meta:
        verbose_name='Festival'
        verbose_name_plural='Festivales'
    def __str__(self):
        return '%s' %(self.nombre)

@receiver(post_delete, sender=Festival)
def imagen(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen.delete(False)



class FestivalFotos(models.Model):
    categoria = models.ForeignKey(Festival)
    nombre_foto = models.CharField(max_length=100)
    imagen_festival = models.ManyToManyField(ContenidoGaleriaFestival)
    class Meta:
        verbose_name='Festival Foto'
        verbose_name_plural='Festival Fotos'
    def __str__(self):
        return '%s' %(self.nombre_foto)


class Fiesta(models.Model):
    nombre= models.CharField(max_length=200)
    fecha= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=5000)
    imagen  = models.ImageField(upload_to='fiestaTemas/')

    class Meta:
        verbose_name='Fiesta'
        verbose_name_plural='Fiestas'
    def __str__(self):
        return '%s' %(self.nombre)

@receiver(post_delete, sender=Fiesta)
def imagen(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.imagen.delete(False)


class FiestaFotos(models.Model):
    categoria = models.ForeignKey(Fiesta)
    nombre_foto = models.CharField(max_length=100)
    imagen_fiesta = models.ManyToManyField(ContenidoGaleriaFiesta)
    class Meta:
        verbose_name='Fiesta Foto'
        verbose_name_plural='Fiesta Fotos'
    def __str__(self):
        return '%s' %(self.nombre_foto)

class Concejo(models.Model):
	nombre_alcalde = models.CharField(max_length=255)
	nombre_sindico = models.CharField(max_length=255)
	nombre_PRP = models.CharField(max_length=255)
	nombre_SRP = models.CharField(max_length=255)
	nombre_TRP = models.CharField(max_length=255)
	nombre_CRP = models.CharField(max_length=255)
	nombre_PRS = models.CharField(max_length=255)
	nombre_SRS = models.CharField(max_length=255)
	nombre_TRS = models.CharField(max_length=255)
	nombre_CRS = models.CharField(max_length=255)

	class Meta:
		verbose_name='Concejo municipal'
		verbose_name_plural = 'Concejos municipales'
	def __str__(self):
		return '%s' %(self.nombre_alcalde)

class DiscursoAlcalde(models.Model):
	discurso_alcalde = models.TextField(max_length=255)
	class Meta:
		verbose_name='Discurso del alcalde'
		verbose_name_plural = 'Discursos del alcalde'
	def __str__(self):
		return '%s' %(self.discurso_alcalde)
