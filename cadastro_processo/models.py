from csv import reader
from io import TextIOWrapper
from django.db import models
from processo.models import Processo


class Planilha(models.Model):
    nome = models.CharField(max_length=30)
    cliente = models.CharField(max_length=30)
    arquivo = models.FileField(upload_to="arquivos")

    def registra_processo(self):
        # recebe arquivo do FileField
        arquivoF = TextIOWrapper(self.arquivo.file)
        # separa itens pelo ';'
        leitor = reader(arquivoF, delimiter=';')
        next(leitor)  # pula primeira linha de headers do csv

        for linha in leitor:
            # cria Processo com infos de uma linha
            Processo.objects.create(
                pasta=linha[0], comarca=linha[1], uf=linha[2])

    # adiciona registra_processo ao save padrão
    # sempre executa essa ação, na criação ou edição
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.registra_processo()

    def __str__(self):
        return self.nome
