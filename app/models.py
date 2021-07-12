from django.db import models
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    order_of_display = models.SmallIntegerField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image = models.CharField(max_length=1000, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField()
    # available = models.BooleanField(default=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)





"""
from django.db import models
from django.contrib.auth.models import User


# Класс категорий
class Category(models.Model):
    # Независимые параметры
    name = models.CharField(max_length=100,
                            db_index=True)
    slug = models.CharField(max_length=100,
                            unique=True)

    class Meta:
        ordering = ('slug',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# Класс продуктов
class Product(models.Model):
    # Зависимые параметры
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    # Незавсисимые параметры
    slug = models.SlugField(max_length=200,
                            unique=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    name = models.CharField(max_length=200,
                            db_index=True)
    imageURL = models.TextField(blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


# Класс корзины
class Cart(models.Model):
    # Зависимые параметры
    slug = models.ForeignKey(Product.slug,
                             related_name='cart',
                             on_delete=models.CASCADE)

    # Незавсисимые параметры
    total_price = models.ImageField(max_digits=10,
                                    decimal_places=2,
                                    default=0)
    phone_number = models.CharField(max_length=48,
                                    blank=True,
                                    null=True,
                                    default=None)
    mail = models.EmailField(blank=True,
                             null=True,
                             default=None)
    user = models.ForeignKey(User,
                             blank=True,
                             null=True,
                             default=None,
                             on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    name = models.CharField(max_length=200,
                            db_index=True)
    adress = models.TextField(blank=True)

    def __str__(self):
        return self.Product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.Product.price
        self.total_price = int(self.quantity) * price_per_item

        super(Cart, self).save(*args, **kwargs)


# Класс пользователей
class Users(models.Model):
    # Зависимые параметры
    phone_number = models.ForeignKey(Cart,
                                     related_name='users',
                                     on_delete=models.CASCADE)
    mail = models.ForeignKey(Cart,
                             related_name='users',
                             on_delete=models.CASCADE)
    name = models.models.ForeignKey(Cart,
                                    related_name='users',
                                    on_delete=models.CASCADE)
    adress = models.ForeignKey(Cart,
                               related_name='users',
                               on_delete=models.CASCADE)

    # Незавсисимые параметры
    password = models.CharField(max_length=200,
                                db_index=True)
    comment = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        super(Users , self).save(*args, **kwargs)
"""