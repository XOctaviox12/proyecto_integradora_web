from django.contrib import admin
from .models import Explorador

@admin.register(Explorador)
class ExploradorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'fecha_registro')
    search_fields = ('nombre', 'correo')
    list_filter = ('fecha_registro',)
    ordering = ('-fecha_registro',)
    readonly_fields = ('fecha_registro',)

    def has_add_permission(self, request):
        # Solo el superusuario puede agregar registros manualmente
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        # Solo el superusuario puede editar registros
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        # Solo el superusuario puede eliminar registros
        return request.user.is_superuser
