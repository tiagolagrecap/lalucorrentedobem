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
    phone = PhoneField(null=True, E164_only=False, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    refer = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name
