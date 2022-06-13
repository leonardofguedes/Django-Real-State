from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Imovel(models.Model):
    FINAN = (
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('Indefinido', 'Não informado')
    )
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=265)
    slug = models.SlugField()
    financible = models.CharField(choices=FINAN, blank=False, null=False, default='U', max_length=15)
    area = models.IntegerField()
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    street = models.CharField(max_length=165)
    district = models.CharField(max_length=25)
    city = models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='imoveis/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


    def __str__(self):
        return self.title