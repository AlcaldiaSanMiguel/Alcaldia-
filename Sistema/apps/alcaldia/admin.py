from django.contrib import admin

# Register your models here.
from .models import *
from django.forms import Textarea

#Ovidio

class MensajeAdmin(admin.ModelAdmin):
	readonly_fields=('nombre','email','mensaje')
	list_display = ('nombre','email','mensaje')

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
	list_display = ('categoria','nombre_foto')

class ComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','imagen')


class ComidaFotosAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_foto')

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','imagen')

class FestivalFotoAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_foto')

class FiestaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','imagen')

class FiestaFotoAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre_foto')

class NoticiasAdmin(admin.ModelAdmin):
	list_display = ('nombre_noticia','descripcion','imagen_descriptiva')

class TasaAdmin(admin.ModelAdmin):
	list_display = ('nombre_tasa','tipo','monto')

class ProgramaAdmin(admin.ModelAdmin):
	list_display = ('nombre_programa','titulo','descripcion','imagenes_asociadas')

class ProyectoAdmin(admin.ModelAdmin):
	list_display = ('tipo_proyecto','titulo','descripcion','imagenes_asociadas')

class TipoProyectoAdmin(admin.ModelAdmin):
	list_display=('tipo_proyecto',)


class DocumentoAdmin(admin.ModelAdmin):
	list_display=('nombre_documento','archivo')


class HermanamientoAdmin(admin.ModelAdmin):
	list_display = ('descripcion','imagenes_asociadas')
class ConcejoAdmin(admin.ModelAdmin):
	
	list_display=('nombre_alcalde', 'nombre_sindico', 'nombre_PRP', 'nombre_SRP', 'nombre_TRP', 'nombre_CRP', 'nombre_PRS', 'nombre_SRS', 'nombre_TRS', 'nombre_CRS',)


class DiscursoAlcaldeAdmin(admin.ModelAdmin):
	list_display=('discurso_alcalde',)


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
admin.site.register(Tasas,TasaAdmin)
admin.site.register(Programa,ProgramaAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(TipoProyecto,TipoProyectoAdmin)
admin.site.register(Documento,DocumentoAdmin)
admin.site.register(Hermanamientos,HermanamientoAdmin)
admin.site.register(Concejo,ConcejoAdmin)	
admin.site.register(DiscursoAlcalde,DiscursoAlcaldeAdmin)



#class TipoTasaAdmin(admin.ModelAdmin):
	#list_display = ('nombre_tipo',)


#admin.site.register(TipoTasa,TipoTasaAdmin)

admin.site.site_header = 'Administracion de contenido de Alcaldia de San Miguel Tepezontes'














