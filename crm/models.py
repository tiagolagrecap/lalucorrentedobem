from django.db import models
from phone_field import PhoneField

# Create your models here.


class Customer(models.Model):
    STATUS = (
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluido', 'Concluido'),
    )

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    refer = models.CharField(max_length=20, null=True, blank=False)
    contact = models.CharField(max_length=20, null=True, blank=False)
    text = models.TextField(null=True, blank=False)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name
