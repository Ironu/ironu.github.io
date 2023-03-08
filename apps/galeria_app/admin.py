from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Categoria,CategoriasAdmin)

class ArtworksAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','img','video')
    search_fields = ('titulo','autor','img','fecha_de_creacion','video')
    list_per_page = 25

    readonly_fields = ['artwork_img']

    def artwork_img(self,obj):
        return mark_safe(
            '<a href="{0}"><img src_"{0}" width="30%"></a>'.format(self.img.url)
        )


admin.site.register(Artwork,ArtworksAdmin)