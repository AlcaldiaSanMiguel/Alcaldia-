from django.contrib import admin

from .models import *
from django.forms import Textarea

# Register your models here.
class ContenidoGaleriaAdmin(admin.ModelAdmin):
	list_display = ('nombre_foto','imagen_galeria')

class ContenidoGaleriaComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre_foto','imagen_galeria')

class ContenidoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_foto','imagen_galeria')

class ContenidoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_foto','imagen_galeria')

class ContenidoAdmin(admin.ModelAdmin):
	#def get_model_perms(self, request):

		list_display = ('nombre_contenido','imagen_contenido')
	#	return { }
class ContenidoProyectoAdmin(admin.ModelAdmin):
	#def get_model_perms(self, request):
		#list_display = ('nombre_contenido','imagen_contenido')
		#return {}
	list_display = ('nombre_Contproyecto','imagen_Contproyecto')




admin.site.register(ContenidoGaleriaTurismo,ContenidoGaleriaAdmin)	
admin.site.register(ContenidoGaleriaComida,ContenidoGaleriaComidaAdmin)  
admin.site.register(ContenidoGaleriaFestival,ContenidoGaleriaAdmin)  
admin.site.register(ContenidoGaleriaFiesta,ContenidoGaleriaAdmin) 
admin.site.register(ContenidoPrograma,ContenidoAdmin)
admin.site.register(ContenidoProyecto,ContenidoProyectoAdmin)