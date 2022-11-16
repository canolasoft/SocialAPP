"""apitest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# myapi/urls.py
from django.urls import include, path
#from rest_framework import routers
from myapi.views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	############# serializers
	# consulta 0: dame los Datos de la app
	path('qry0/', DatappViewSet.as_view({'get': 'list'}), name='qry0'),

	# consulta 1: dame todos los Canales
	path('qry1/', CanalesViewSet.as_view({'get': 'list'}), name='qry1'),

	# consulta 2: dame todas las entradas de un canal (id)
	path('qry2/', EntradasSerializer.as_view(), name='qry2'),

	# consulta 3: dame todos los datos de un canal (id)
	path('qry3/', CanalViewSet.as_view({'get': 'list'}), name='qry3'),

	# consulta 4: dame todas las redes de un canal (id)
	path('qry4/', RedsocialSerializer.as_view(), name='qry4'),

	# consulta 5: dame los datos de una entrada (id)
	path('qry5/', EntradaSerializer.as_view(), name='qry5'),

	# consulta 6: dame todos los textos de una entrada (id)
	path('qry6/', TextoEntradaSerializer.as_view(), name='qry6'),


	############# LANDING
	# Home index
	path('', index, name=""),

	# Canal
	path('canal', canal, name="canal"),
]

