from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Campos que quieres ver en la lista
    list_filter = ('created_at', 'author')           # Filtros en el panel lateral
    search_fields = ('title', 'subtitle', 'content') # Buscador en el admin
    prepopulated_fields = {'slug': ('title',)}       # El slug se autocompleta desde el título
    readonly_fields = ('created_at',)                 # No editable, solo mostrar
