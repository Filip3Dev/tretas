from django.db import models
from decimal import Decimal

class Coinlist(models.Model):
    SHIRT_SIZES = (
        ('1', 'Bittrex'),
        ('2', 'Cryptopia'),
        ('3', 'Novaexchange'),
        ('4', 'Yobit'),
        ('5', 'CCex'),
    )
    name = models.CharField("Nome",max_length=255, blank=False)
    nick = models.CharField("Sigla", max_length=10, blank=False)
    ammount = models.IntegerField("Quantidade de Moedas", blank=False)
    worth = models.DecimalField("Valor Total", max_digits=24, decimal_places=8,default=Decimal('0.00000000'))
    roi = models.IntegerField("ROI", blank=False)
    logo = models.CharField("Imagem da Moeda", max_length=500, blank=False)
    exchange = models.CharField(max_length=1, choices=SHIRT_SIZES)
    price = models.DecimalField("Valor em Bitcoin", max_digits=24, decimal_places=8,default=Decimal('0.00000000'))
    weekcoins = models.DecimalField("Moedas geradas na semana", max_digits=10, decimal_places=5)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nick

class Details(models.Model):
    data = models.ForeignKey(Coinlist)
    nodesconf = models.CharField("node.conf",max_length=855)
    bootstrap = models.CharField("blockchain",max_length=855)
    nodecount = models.IntegerField("Quantidade de Nodes")
    coinslocked = models.IntegerField("Moedas Travadas")
    sharetime = models.TimeField("Tempo entre Shares")
    mcap = models.CharField("Link do Marketcap", max_length=255)
    def __str__(self):
        return self.mcap
# Create your models here.
