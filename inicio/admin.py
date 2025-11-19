from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Estadisticas, PageVisit, Jugadores, ComentarioContacto


admin.site.site_header = "Panel de Administración - Comunidad del Juego"
admin.site.index_title = "Gestión y Monitoreo del Sitio"
admin.site.site_title = "Administrador del Juego"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "login_count", "ver_usuario")
    search_fields = ("user__username",)
    ordering = ("-login_count",)
    list_per_page = 20

    @admin.display(description="Ver en admin de usuarios")
    def ver_usuario(self, obj):
        return format_html(f'<a href="/admin/auth/user/{obj.user.id}/change/"> Abrir</a>')

@admin.register(Estadisticas)
class EstadisticasAdmin(admin.ModelAdmin):
    list_display = ("visitas_home", "registros_exitosos", "eficiencia")
    readonly_fields = ("visitas_home", "registros_exitosos")
    list_per_page = 10

    @admin.display(description="Tasa de conversión (%)")
    def eficiencia(self, obj):
        try:
            return round((obj.registros_exitosos / obj.visitas_home) * 100, 2)
        except ZeroDivisionError:
            return 0.0

@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ("id", "count", "ultima_actualizacion")
    ordering = ("-count",)
    list_per_page = 10

    @admin.display(description="Última actualización")
    def ultima_actualizacion(self, obj):
        return obj._state.db  


@admin.register(Jugadores)
class JugadoresAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "fecha_registro", "dias_desde_registro", "ver_correo")
    search_fields = ("username", "email")
    list_filter = ("fecha_registro",)
    ordering = ("-fecha_registro",)
    readonly_fields = ("fecha_registro",)
    list_per_page = 25

    @admin.display(description="Correo directo")
    def ver_correo(self, obj):
        return format_html(f'<a href="mailto:{obj.email}">Enviar</a>')

    @admin.display(description="Días desde registro")
    def dias_desde_registro(self, obj):
        from datetime import datetime, timezone
        dias = (datetime.now(timezone.utc) - obj.fecha_registro).days
        return f"{dias} días"

@admin.register(ComentarioContacto)
class ComentarioContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "mensaje_corto", "fecha_envio")
    search_fields = ("nombre", "email", "mensaje")
    list_filter = ("fecha_envio",)
    ordering = ("-fecha_envio",)
    readonly_fields = ("nombre", "email", "mensaje", "fecha_envio")

    def mensaje_corto(self, obj):
        return (obj.mensaje[:50] + "...") if len(obj.mensaje) > 50 else obj.mensaje
    mensaje_corto.short_description = "Mensaje"


admin.site.enable_nav_sidebar = True
