from django.contrib import admin
from .models import *

class CanalAdmin(admin.ModelAdmin):
	list_display = ('id_c', 'nombre_c', 'imagen_c', 'descripcion_c', 'id_tag')
admin.site.register(Canal, CanalAdmin)

class RedsocialAdmin(admin.ModelAdmin):
	list_display = ('id_rs', 'id_c', 'nombre_rs', 'imagen_rs', 'url_rs')
admin.site.register(Redsocial, RedsocialAdmin)

class EntradaAdmin(admin.ModelAdmin):
	list_display = ('id_e', 'id_c', 'nombre_e', 'imagen_e', 'url_e', 'id_tag', 'descripcion_e')
admin.site.register(Entrada, EntradaAdmin)

class TextoAdmin(admin.ModelAdmin):
	list_display = (
		'id_t',
		'id_e',
		'texto_t',
		#'imagen_t'
	)
admin.site.register(Texto, TextoAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ('id_tag', 'genero_tag', 'idioma_tag', 'imagen_tag')
admin.site.register(Tag, TagAdmin)

#class RedsocialArtistaAdmin(admin.ModelAdmin):
#	list_display = ('id_rs', 'id_a', 'url_rsa', 'imagen_rs')
#admin.site.register(RedsocialArtista, RedsocialArtistaAdmin)

#class WallpaperAdmin(admin.ModelAdmin):
#	list_display = ('id_w', 'nombre_w', 'imagen_w', 'id_a')
#admin.site.register(Wallpaper, WallpaperAdmin)

class DatappAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulomapp', 'mensajeapp', 'linkapp', 'keyapp', 'iconapp')
admin.site.register(Datapp, DatappAdmin)