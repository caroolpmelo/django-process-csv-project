from django.contrib import admin
from processo.models import Processo
from cadastro_processo.models import Planilha


class Planilhas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cliente', 'arquivo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cliente', 'arquivo')


admin.site.register(Planilha, Planilhas)
