from asyncio.log import logger
from rest_framework import viewsets
import django_filters
import logging
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import(ListCreateAPIView)

# Consulta 0: dame los datos de la app
class DatappViewSet(viewsets.ModelViewSet):
	#queryset = Datapp.objects.all()
	serializer_class = DatappSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		return Datapp.objects.filter(keyapp = kap)

# Consulta 1: dame todos los Canales
class CanalesViewSet(viewsets.ModelViewSet):
	serializer_class = CanalSerializer
	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			return Canal.objects.all().order_by('nombre_c')

# Consulta 2: dame todas las Entradas de un Canal
class EntradasSerializer(ListCreateAPIView):
	serializer_class = EntradasSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_c = self.request.GET.get('id')
			entradas = Entrada.objects.filter(id_c__id_c = id_c)
			return entradas

# Consulta 2: dame todos los Wallpapers de un Artista
#class WallpaperSerializer(ListCreateAPIView):
#	serializer_class = WallpaperSerializer
#
#	def get_queryset(self):
#		kap = self.request.GET.get('kap')
#		if(Datapp.objects.filter(keyapp = kap)):
#			id_a = self.request.GET.get('id')
#			wallpapers = Wallpaper.objects.filter(id_a__id_a = id_a)
#			return wallpapers

# Consulta 3: dame los datos de un Canal
class CanalViewSet(viewsets.ModelViewSet):
	serializer_class = CanalSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_c = self.request.GET.get('id')
			return Canal.objects.filter(id_c = id_c)

# Consulta 4: dame las Redes de un Canal
class RedsocialSerializer(ListCreateAPIView):
	serializer_class = RedsocialSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_c = self.request.GET.get('id')
			redesociales = Redsocial.objects.filter(id_c__id_c = id_c)
			return redesociales

# Consulta 5: dame los datos de un Video
class EntradaSerializer(ListCreateAPIView):
	serializer_class = EntradaSerializer

	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_e = self.request.GET.get('id')
			entrada = Entrada.objects.filter(id_e = id_e)
			return entrada

class TextoEntradaSerializer(ListCreateAPIView):
	serializer_class = TextoEntradaSerializer
	def get_queryset(self):
		kap = self.request.GET.get('kap')
		if(Datapp.objects.filter(keyapp = kap)):
			id_e = self.request.GET.get('id')
			logging.error("id_e: "+id_e)
			#entrada = Entrada.objects.filter(id_e = id_e).first()
			textos = Texto.objects.filter(id_e = id_e)
			return textos

#### LANDING

# Home index: muestra todos los canales
def index(request):
	canales = Canal.objects.all().order_by('nombre_c')
	context = {'canales':canales}
	return render(request, "landing/index.html", context)

# Canal: muestra los datos y entradas de un canal
def canal(request):
	texto_t = str(request.POST.get('texto_t'))
	id_e = request.POST.get('id_e')
	logger.error("texto_t: "+texto_t+". id_e: "+str(id_e))
	if texto_t != 'None':
		id_c = request.POST.get('id')
		entrada = Entrada.objects.filter(id_e = id_e).first()
		texto = Texto.objects.create(
			id_e = entrada,
			texto_t = texto_t,
		)
		texto.save()
	else:
		id_c = request.GET.get('id')
	canal = Canal.objects.filter(id_c = id_c).first
	logger.error("canal: "+str(canal))
	entradas = Entrada.objects.filter(id_c = id_c)
	textos = Texto.objects.filter(id_e__id_c = id_c)
	context = {
		'canal':canal,
        'entradas':entradas,
        'textos':textos,
        }
	return render(request, "landing/canal.html", context)