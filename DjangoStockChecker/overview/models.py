from django.db import models

class Account(models.Model):
    """
        User Account for the Stock Checker System
        Conta de um Usuário para o Sistema de Monitoramento de Ações
    """

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(min_length=8, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Stock(models.Model):
    """
        Stock Model, with the Tuneling Parameters and Frequency of the Check
        Modelo de Ações, com os Parâmetros de Tunelamento e Frequência de Checagem
    """

    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE) # 1 to Many
    # When deleting an Account, it's Stocks are also deleted
    # Ao deletar uma Conta, suas Ações também são deletadas
    ticker = models.CharField(max_length=10)
    minimum_value = models.FloatField()
    maximum_value = models.FloatField()
    check_frequency_in_minutes = models.IntegerField() # In minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticker
