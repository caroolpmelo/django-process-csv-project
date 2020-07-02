from django.db import models


class Processo(models.Model):
    pasta = models.CharField(max_length=30)
    comarca = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.pasta
