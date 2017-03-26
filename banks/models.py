from django.db import models


class Bank(models.Model):

    name = models.CharField(max_length=250)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=19, decimal_places=10)
    safe = models.DecimalField(max_digits=19, decimal_places=10)
    info = models.DecimalField(max_digits=19, decimal_places=10)
    service = models.DecimalField(max_digits=19, decimal_places=10)
    add_service = models.DecimalField(max_digits=19, decimal_places=10)
    investments = models.DecimalField(max_digits=19, decimal_places=10)
    transfers = models.DecimalField(max_digits=19, decimal_places=10)
    accounts = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    bank_contact = models.DecimalField(max_digits=19, decimal_places=10)
    terminal_availability = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.name


class Bank_Ul(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=19, decimal_places=10)
    info = models.DecimalField(max_digits=19, decimal_places=10)
    bank_contact = models.DecimalField(max_digits=19, decimal_places=10)
    business_func = models.DecimalField(max_digits=19, decimal_places=10)
    safe = models.DecimalField(max_digits=19, decimal_places=10)
    currency_work = models.DecimalField(max_digits=19, decimal_places=10)

    def __str__(self):
        return self.name
