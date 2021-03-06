from __future__ import unicode_literals
from __future__ import absolute_import
from django.db.models.signals import post_delete
from django.dispatch import receiver

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from django.db import models

from apps.gestion.models import *

# Definicion de todos los modelos a utilizar en la base de datos

class Mensaje(models.Model):
	nombre = models.CharField(max_length=30)
	email  = models.CharField(max_length=50)
	mensaje = models.TextField(max_length=500)
	class Meta:
		verbose_name='Mensaje'
		verbose_name_plural='Mensajes'
	def __str__(self):
		return '%s' %(self.nombre)


class ContactosEmergencia(models.Model):
	nombre_contacto = models.CharField(max_length=30, unique=True)
	telefono=models.CharField(max_length=9)
	class Meta:
		verbose_name='Contacto de emergencia'
		verbose_name_plural='Contactos de emergencia'
	def __str__(self):
		return '%s' %(self.nombre_contacto)


class Noticias(models.Model):
	nombre_noticia = models.CharField(max_length=100, unique=True)
	descripcion = models.TextField(max_length=2000)
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
	nombre_programa = models.CharField(max_length=80, unique=True)
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=5000)
	imagen  = models.ManyToManyField(ContenidoPrograma)

	def imagenes_asociadas(self):
		return "\n".join([i.nombre_contenido for i in self.imagen.all()])

	class Meta:
		verbose_name='Programa'
		verbose_name_plural='Programas'
	def __str__(self):
		return '%s' %(self.nombre_programa)

class TipoProyecto(models.Model):
	tipo_proyecto = models.CharField(max_length=80, unique=True)
	class Meta:
		verbose_name='Tipo proyecto'
		verbose_name_plural = 'Tipos proyectos'
	def __str__(self):
		return '%s' %(self.tipo_proyecto)

class Proyecto(models.Model):
	tipo_proyecto = models.ForeignKey(TipoProyecto)
	titulo = models.CharField(max_length=200)
	descripcion = models.TextField(max_length=500)
	imagen  = models.ManyToManyField(ContenidoProyecto)
	fecha  = models.DateField(null=True)

	def imagenes_asociadas(self):
		return "\n".join([i.nombre_Contproyecto for i in self.imagen.all()])

	class Meta:
		verbose_name='Proyecto'
		verbose_name_plural='Proyectos'
	def __str__(self):
		return '%s' %(self.tipo_proyecto)

class TipoTasa(models.Model):
	nombre_tipo = models.CharField(max_length=80, unique=True)
	class Meta:
		verbose_name='Tipo tasa municipal'
		verbose_name_plural = 'Tipo tasas municipales'
	def __str__(self):
		return '%s' %(self.nombre_tipo)


class Tasas(models.Model):
	tipo = models.ForeignKey(TipoTasa)
	nombre_tasa = models.CharField(max_length=80)
	monto = models.CharField(max_length=60)

	class Meta:
		verbose_name='Tasa municipal'
		verbose_name_plural = 'Tasas Municipales'
	def __str__(self):
		return '%s' %(self.nombre_tasa)

class Documento(models.Model):
	nombre_documento = models.CharField(max_length=100, unique=True)
	archivo = models.FileField(upload_to='documentos/')

	class Meta:
		verbose_name='Documento'
		verbose_name_plural='Documentos'
	def __str__(self):
		return '%s' %(self.nombre_documento)

class Hermanamientos(models.Model):
	descripcion = models.TextField(max_length=1000)
	imagen  = models.ManyToManyField(ContenidoPrograma)

	def imagenes_asociadas(self):
		return "\n".join([i.nombre_contenido for i in self.imagen.all()])

	class Meta:
		verbose_name='Hermanamiento'
		verbose_name_plural='Hermanamientos'
	def __str__(self):
		return '%s' %(self.descripcion)


class Historia(models.Model):
	titulo_historia = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=5000)
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
	descripcion = models.TextField(max_length=5000)
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
	nombre_galeria = models.CharField(max_length=100)
	turismo_fotos = models.ManyToManyField(ContenidoGaleriaTurismo)
	class Meta:
		verbose_name='Turismo Foto'
		verbose_name_plural='Turismo Fotos'
	def __str__(self):
		return '%s' %(self.nombre_galeria)


class Comida(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion = models.TextField(max_length=5000)
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
    nombre_galeria = models.CharField(max_length=100)
    comida_fotos = models.ManyToManyField(ContenidoGaleriaComida)
    class Meta:
        verbose_name='ComidaFoto'
        verbose_name_plural='Comida Fotos'
    def __str__(self):
        return '%s' %(self.nombre_galeria)


class Festival(models.Model):
    nombre= models.CharField(max_length=200)
    descripcion = models.TextField(max_length=5000)
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
    nombre_galeria = models.CharField(max_length=100)
    festival_fotos = models.ManyToManyField(ContenidoGaleriaFestival)
    class Meta:
        verbose_name='Festival Foto'
        verbose_name_plural='Festival Fotos'
    def __str__(self):
        return '%s' %(self.nombre_galeria)


class Fiesta(models.Model):
    nombre= models.CharField(max_length=200)
    fecha= models.CharField(max_length=100)
    descripcion = models.TextField(max_length=5000)
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
    nombre_galeria = models.CharField(max_length=100)
    fiesta_fotos = models.ManyToManyField(ContenidoGaleriaFiesta)
    class Meta:
        verbose_name='Fiesta Foto'
        verbose_name_plural='Fiesta Fotos'
    def __str__(self):
        return '%s' %(self.nombre_galeria)


class Rol(models.Model):
	nombre_rol = models.CharField(max_length=100, unique=True)
	class Meta:
		verbose_name='Rol'
		verbose_name_plural='Roles'
	def __str__(self):
		return '%s' %(self.nombre_rol)

class Concejo(models.Model):
	nombre_persona = models.CharField(max_length=255)
	rol = models.ForeignKey(Rol)
	class Meta:
		verbose_name='Concejo municipal'
		verbose_name_plural = 'Concejos municipales'
	def __str__(self):
		return '%s' %(self.nombre_persona)


class DiscursoAlcalde(models.Model):
	discurso_alcalde = models.TextField(max_length=1500)
	class Meta:
		verbose_name='Discurso del alcalde'
		verbose_name_plural = 'Discursos del alcalde'
	def __str__(self):
		return '%s' %(self.discurso_alcalde)

class Cargo(models.Model):
	nombre_cargo = models.CharField(max_length=100, unique=True)
	class Meta:
		verbose_name='Cargo'
		verbose_name_plural='Cargos'
	def __str__(self):
		return '%s' %(self.nombre_cargo)

class Nomina(models.Model):
	nombre_empleado = models.CharField(max_length=255)
	cargo = models.ForeignKey(Cargo)
	class Meta:
		verbose_name_plural = 'Nomina de empleados'
	def __str__(self):
		return '%s' %(self.nombre_empleado)
