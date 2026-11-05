from django.contrib import admin
from .models import Categoria, LugarPatrimonial

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ubicacion', 'anio_construccion', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'ubicacion')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(LugarPatrimonial, LugarPatrimonialAdmin)
