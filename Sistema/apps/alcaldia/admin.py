from django.contrib import admin

# Register your models here.
from .models import *
from django.forms import Textarea
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

class MensajeAdmin(admin.ModelAdmin):
	readonly_fields=('nombre','email','mensaje')
	list_display = ('nombre','email','mensaje')
	def has_add_permission(self, request):
		return False

class ContactoAdmin(admin.ModelAdmin):
	list_display = ('nombre_contacto','telefono')

class HistoriaAdmin(admin.ModelAdmin):
	formfield_overrides={
	models.CharField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
	}
	list_display = ('titulo_historia','descripcion','imagen_descriptiva')

class TurismoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion','imagen')

class TurismoFotosAdmin(admin.ModelAdmin):
	list_display = ('categoria','nombre_galeria')

class ComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','imagen')


class ComidaFotosAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_galeria')

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','imagen')

class FestivalFotoAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_galeria')

class FiestaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','imagen')

class FiestaFotoAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_galeria')

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('nombre_noticia','descripcion','imagen_descriptiva')

# class TipoTasaAdmin(admin.ModelAdmin):
# 	def get_model_perms(self, request):
# 		return {}
# 	#list_display = ('nombre_tipo',)

class TasaAdmin(admin.ModelAdmin):
	list_display = ('nombre_tasa','tipo','monto')

class ProgramaAdmin(admin.ModelAdmin):
	list_display = ('nombre_programa','titulo','descripcion','imagenes_asociadas')

class ProyectoAdmin(admin.ModelAdmin):
	list_display = ('tipo_proyecto','titulo','descripcion','imagenes_asociadas')

class TipoProyectoAdmin(admin.ModelAdmin):
	def get_model_perms(self, request):
		return {}
	#list_display=('tipo_proyecto',)


class DocumentoAdmin(admin.ModelAdmin):
	list_display=('nombre_documento','archivo')
	def has_add_permission(self, request):
		return False

	def get_actions(self, request):
		actions = super(DocumentoAdmin, self).get_actions(request)
		del actions['delete_selected'] 
		return actions

	def has_delete_permission(self, request, obj=None):
		return False


class HermanamientoAdmin(admin.ModelAdmin):
	list_display = ('descripcion','imagenes_asociadas')

class ConcejoAdmin(admin.ModelAdmin):
	list_display=('nombre_persona','rol',)

class RolAdmin(admin.ModelAdmin):
	def get_model_perms(self, request):
		return {}

class DiscursoAlcaldeAdmin(admin.ModelAdmin):
	list_display=('discurso_alcalde',)
	def has_add_permission(self, request):
		return False

	def get_actions(self, request):
		actions = super(DiscursoAlcaldeAdmin, self).get_actions(request)
		del actions['delete_selected'] 
		return actions

	def has_delete_permission(self, request, obj=None):
		return False
		
class NominaAdmin(admin.ModelAdmin):
	list_display=('nombre_secretaria','nombre_auditor','nombre_contador','nombre_info_publica','nombre_UACI','nombre_tesorero','nombre_cuentas_corrientes','nombre_estado_familiar','nombre_medio_ambiente','nombre_proyeccion','nombre_atencion','nombre_motorista','nombre_ordenanza','nombre_mantenimiento','nombre_mantenimiento2','nombre_vigilante','nombre_vigilante2','nombre_vigilante3')

class CargoAdmin(admin.ModelAdmin):
	def get_model_perms(self, request):
		return {}

class NominaAdmin(admin.ModelAdmin):
	list_display = ('nombre_empleado','cargo',)

admin.site.register(Mensaje,MensajeAdmin)
admin.site.register(ContactosEmergencia,ContactoAdmin)
admin.site.register(Historia,HistoriaAdmin)
admin.site.register(Turismo,TurismoAdmin)
admin.site.register(TurismoFotos,TurismoFotosAdmin)
admin.site.register(Comida,ComidaAdmin)
admin.site.register(ComidaFotos,ComidaFotosAdmin)
admin.site.register(Festival,FestivalAdmin)
admin.site.register(FestivalFotos,FestivalFotoAdmin)
admin.site.register(Fiesta,FiestaAdmin)
admin.site.register(FiestaFotos,FiestaFotoAdmin) 
admin.site.register(Noticias,NoticiasAdmin)
#admin.site.register(TipoTasa,TipoTasaAdmin)
admin.site.register(Tasas,TasaAdmin)
admin.site.register(Programa,ProgramaAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(TipoProyecto,TipoProyectoAdmin)
admin.site.register(Documento,DocumentoAdmin)
admin.site.register(Hermanamientos,HermanamientoAdmin)
admin.site.register(Rol,RolAdmin)	
admin.site.register(Concejo,ConcejoAdmin)
admin.site.register(DiscursoAlcalde,DiscursoAlcaldeAdmin)
admin.site.register(Cargo,CargoAdmin)
admin.site.register(Nomina,NominaAdmin)


#cabecera de la administracion 
admin.site.site_header = 'Administracion de contenido de Alcaldia de San Miguel Tepezontes'














