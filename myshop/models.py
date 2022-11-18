from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.urls import reverse
from django.utils import timezone


class MyUser(AbstractUser):
    cash = models.IntegerField(blank=True, null=True, verbose_name='cash')

    # def save(self, *args, **kwargs):
    #     user = super(MyUser, self)
    #     user.set_password(self.password)
    #     user.save()
    #     return user


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(blank=True)
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('myshop:site_product', args=[self.name])

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(default=timezone.now)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product_id} | {self.quantity}'


class Return(models.Model):
    delete_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    # created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.delete_id}'


