from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import *

# Create your views here.

def autoridades(request):
		return render(request, 'Transparencia/autoridades.html',{})

def alumbrado(request):
	alumbrado_list = Proyecto.objects.filter(tipo_proyecto = "4").order_by('-fecha')
	paginador = Paginator(alumbrado_list, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		alumbrado = paginador.page(page)
	except(EmptyPage, InvalidPage):
		alumbrado = paginador.page(paginador.num_pages)
	return render(request, 'Proyectos/alumbrado.html',{'alumbrados':alumbrado})

def comida(request):
	comida=Comida.objects.all()
	paginador = Paginator(comida, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		comida = paginador.page(page)
	except(EmptyPage, InvalidPage):
		comida = paginador.page(paginador.num_pages)
	return render(request,'Turismo/comida/comida.html',{'comidas':comida})

def comida_select(request, id_comida):
    try:

        comida = Comida.objects.get(id=id_comida)
        galeria = ComidaFotos.objects.filter(categoria_id=id_comida)
    except ComidaFotos.DoesNotExist:
       raise Http404

    return render(request, 'Turismo/comida/detalle_comida.html',{'comida':comida,'galeria':galeria})

def contacto(request):
	contacto = ContactosEmergencia.objects.all()
	if request.method == "POST":
		mensajes = Mensaje()
		mensajes.nombre = request.POST['usuario']
		mensajes.email = request.POST['correo']
		mensajes.mensaje =request.POST['peticion']
		mensajes.save()
		return HttpResponseRedirect('/contactanos')
	return render(request,'Inicio/contactanos.html',{'contactos':contacto})


def Catastro(request):
	return render(request, 'Proyectos/Catastro.html',{})

def concejo(request):
	concejo = Concejo.objects.all()
	return render(request, 'Estructura/concejo.html',{'concejos': concejo})

def desechosSolidos(request):
	desechos_list= Proyecto.objects.filter(tipo_proyecto = "5").order_by('-fecha')
	paginador = Paginator(desechos_list, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		desecho = paginador.page(page)
	except(EmptyPage, InvalidPage):
		desecho = paginador.page(paginador.num_pages)
	return render(request,'Proyectos/desechosSolidos.html',{'desechos':desecho})


def estructura(request):
		return render(request, 'Estructura/estructura.html',{})


def festival(request):
	festival=Festival.objects.all()
	paginador = Paginator(festival, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		festival = paginador.page(page)
	except(EmptyPage, InvalidPage):
		festival = paginador.page(paginador.num_pages)
	return render(request,'Turismo/festival/festival.html',{'festivales':festival})



def festival_select(request, id_festival):
    try:

        festival = Festival.objects.get(id=id_festival)
        galeria = FestivalFotos.objects.filter(categoria_id=id_festival)
    except FestivalFotos.DoesNotExist:
       raise Http404

    return render(request, 'Turismo/festival/detalle_festival.html',{'festival':festival,'galeria':galeria})

def fiesta(request):
	fiesta=Fiesta.objects.all()
	paginador = Paginator(fiesta, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		fiesta = paginador.page(page)
	except(EmptyPage, InvalidPage):
		fiesta = paginador.page(paginador.num_pages)
	return render(request,'Turismo/fiesta/fiestas.html',{'fiestas':fiesta})

def fiesta_select(request, id_fiesta):
    try:

        fiesta = Fiesta.objects.get(id=id_fiesta)
        galeria = FiestaFotos.objects.filter(categoria_id=id_fiesta)
    except FiestaFotos.DoesNotExist:
       raise Http404
    return render(request, 'Turismo/fiesta/detalle_fiestas.html',{'fiesta':fiesta,'galeria':galeria})

def hermanamientos(request):
	hermanamiento = Hermanamientos.objects.all()
	return render(request, 'Hermanamientos/hermanamientos.html',{'hermanamientos':hermanamiento})

def historia(request):
	historia=Historia.objects.all()
	paginador = Paginator(historia, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		historia = paginador.page(page)
	except(EmptyPage, InvalidPage):
		historia = paginador.page(paginador.num_pages)
	return render(request,'Turismo/historia/historia.html',{'historias':historia},)


def index(request):
	documento= Documento.objects.filter(id = "1")
	return render(request,'Inicio/index.html',{'documentos':documento})


def infraestructuraGR(request):
	infraestructuraGR_list = Proyecto.objects.filter(tipo_proyecto = "2").order_by('-fecha')
	paginador = Paginator(infraestructuraGR_list, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		infraestructura = paginador.page(page)
	except(EmptyPage, InvalidPage):
		infraestructura = paginador.page(paginador.num_pages)
	return render(request,'Proyectos/infraestructuraGR.html',{'infraestructuras':infraestructura})


def mantenimientoCalles(request):
	mantenimiento_list = Proyecto.objects.filter(tipo_proyecto = "3").order_by('-fecha')
	paginador = Paginator(mantenimiento_list, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		mantenimiento = paginador.page(page)
	except(EmptyPage, InvalidPage):
		mantenimiento = paginador.page(paginador.num_pages)
	return render(request, 'Proyectos/mantenimientoCalles.html',{'mantenimientos':mantenimiento})

def municipalidad(request):
		return render(request, 'Municipalidad/municipalidad.html',{})


def mensaje(request):
	mensaje = DiscursoAlcalde.objects.all()
	return render(request, 'Inicio/mensaje.html',{'mensajes': mensaje})


def nomina(request):
	nomina = Nomina.objects.all()
	return render(request, 'Estructura/nomina.html',{'nominas': nomina})

def noticias(request):

	noticia_list = Noticias.objects.all().order_by('-id')
	paginador = Paginator(noticia_list, 4)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		noticias = paginador.page(page)
	except(EmptyPage, InvalidPage):
		noticias = paginador.page(paginador.num_pages)
	return render(request, 'Noticias/noticias.html',{'noticias':noticias})


def noticia_select(request, id_noticia):
	try:
		noticia = Noticias.objects.get(id=id_noticia)
	except Noticias.DoesNotExist:
	   raise Http404

	return render(request, 'Noticias/detalle_noticia.html',{'noticia':noticia})

def organigrama(request):
		return render(request, 'Transparencia/organigrama.html',{})

def programas(request):
	programa = Programa.objects.all()

	return render(request, 'Programas/programas.html',{'programas':programa})

def proyectoSocial(request):
	proyectosocial_list = Proyecto.objects.filter(tipo_proyecto = "1").order_by('-fecha')
	paginador = Paginator(proyectosocial_list, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		proyectosocial = paginador.page(page)
	except(EmptyPage, InvalidPage):
		proyectosocial = paginador.page(paginador.num_pages)
	return render(request,'Proyectos/proyectoSocial.html',{'proyectosociales':proyectosocial})

def servicios(request):
	return render(request, 'Inicio/servicios.html',{})


def turismo(request):
	turismo=Turismo.objects.all()
	paginador = Paginator(turismo, 3)
	try:
		page = int(request.GET.get("page",'1'))
	except:
		page = 1
	try:
		turismo = paginador.page(page)
	except(EmptyPage, InvalidPage):
		turismo = paginador.page(paginador.num_pages)
	return render(request,'Turismo/turismo/turismo.html',{'turismos':turismo})

def turismo_select(request, id_turismo):
	try:

		turismo = Turismo.objects.get(id=id_turismo)
		galeria = TurismoFotos.objects.filter(categoria_id=id_turismo)
	except TurismoFotos.DoesNotExist:
	   raise Http404

	return render(request, 'Turismo/turismo/detalle_turismo.html',{'turismo':turismo,'galeria':galeria})


def TasasMunicipales(request):
	tipos = TipoTasa.objects.all()
	return render(request,'Tasas/TasasMunicipales.html',{'tipos':tipos})



def transparencia(request):
	documento= Documento.objects.filter(id = "2")
	return render(request, 'Transparencia/transparencia.html',{'documentos':documento})
