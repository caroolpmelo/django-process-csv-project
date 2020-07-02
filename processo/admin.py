from django.contrib import admin
from processo.models import Processo


class Processos(admin.ModelAdmin):
    list_display = ('id', 'pasta', 'comarca', 'uf')
    list_display_links = ('id', 'pasta')
    search_fields = ('pasta', 'comarca', 'uf')


admin.site.register(Processo, Processos)
