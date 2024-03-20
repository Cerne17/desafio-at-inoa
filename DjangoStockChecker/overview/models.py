from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.urls import reverse

class Stock(models.Model):
    """
        Stock Model, with the Tuneling Parameters and Frequency of the Check
        Modelo de Ações, com os Parâmetros de Tunelamento e Frequência de Checagem
    """

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) # 1 to Many
    # When deleting an Account, it's Stocks are also deleted
    # Ao deletar uma Conta, suas Ações também são deletadas
    ticker = models.CharField(max_length=10, null=False, verbose_name="Ticker da Ação")
    minimum_value = models.FloatField(verbose_name="Valor de Compra")
    maximum_value = models.FloatField(verbose_name="Valor de Venda")
    check_frequency_in_minutes = models.IntegerField() # In minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticker

    def get_absolute_url(self):
        return reverse('stock_detail', args=[str(self.id)])

class StockHistory(models.Model):
    """
        Stock History Model, with the Stock's Hitorical Data.
        Modelo de Histórico de Ações, com os Dados Históricos da Ação.
    """

    id = models.AutoField(primary_key=True, null=False)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, null=False) # 1 to Many
    price = models.FloatField(null=False, verbose_name="Preço da Ação")
    date = models.DateField(default=date.today, null=False, verbose_name="Data de Registro")
