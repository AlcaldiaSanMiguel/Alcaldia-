from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url
from apps.alcaldia.views import *

urlpatterns = [
   url(r'^$', index),





    url(r'^servicios/', servicios),
    url(r'^mantenimientoCalles/', mantenimientoCalles),
    url(r'^alumbrado/', alumbrado),
    #URLS noticias
    url(r'^noticias/$', noticias, name='noticias'),
    url(r'^noticias/detalle/(?P<id_noticia>\d+)/$', noticia_select, name='detalle_noticia'),
    #fin URLS noticias

    #URLS programas
    url(r'^programas/', programas),
    #fin URLS programas

    url(r'^contactanos/', contacto),
    url(r'^comida/$', comida, name='comida'),
    url(r'^comida/detalle_comida/(?P<id_comida>\d+)/$', comida_select, name='detalle_comida'),
    url(r'^historia/', historia),
    url(r'^turismo/$', turismo, name='turismo'),
    url(r'^turismo/detalle_turismo/(?P<id_turismo>\d+)/$', turismo_select, name='detalle_turismo'),
    url(r'^festival/$', festival, name='festival'),
    url(r'^festival/detalle_festival/(?P<id_festival>\d+)/$', festival_select, name='detalle_festival'),
    url(r'^fiestas/$', fiesta, name='fiesta'),
    url(r'^fiesta/detalle_fiesta/(?P<id_fiesta>\d+)/$', fiesta_select, name='detalle_fiesta'),
    url(r'^proyectoSocial/', proyectoSocial),
    url(r'^TasasMunicipales/', TasasMunicipales),
    url(r'^infraestructuraGR/', infraestructuraGR),
    url(r'^transparencia/', transparencia),
    url(r'^organigrama/', organigrama),
    url(r'^autoridades/', autoridades),
    url(r'^municipalidad/', municipalidad),
    url(r'^concejo/', concejo),
    url(r'^mensaje/', mensaje),
    url(r'^estructura/', estructura),
    url(r'^nomina/', nomina),


]
