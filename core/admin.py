from django.contrib import admin
from core.models import Usuario, Compras
# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'email')


admin.site.register(Usuario, UsuarioAdmin)


class ComprasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'valor', 'cpf_compra', 'data', 'percent_cashback', 'cashback', 'status')


admin.site.register(Compras, ComprasAdmin)
