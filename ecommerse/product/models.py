from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='category',
        null=True,
        blank=True,
        verbose_name=_('Parent category')
    )
    image = models.ImageField(upload_to="category_images/", null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='brand',
        related_query_name='brands',
        null=True,
        blank=True
    )
    brand = models.CharField(max_length=250)

    def __str__(self):
        return self.brand


class Color(models.Model):
    color = models.CharField(max_length=250)

    def __str__(self):
        return self.color


class Product(models.Model):
    M = "M"
    F = "F"
    A = "A"

    GENDER_CHOICES = (
        (M, "male"),
        (F, "female"),
        (A, "All"),
    )

    S = "S"
    M = "M"
    L = "L"
    XL = "XL"

    SIZE_CHOICES = (
        (S, "small"),
        (M, "medium"),
        (L, "large"),
        (XL, "xtra large"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='product',
        related_query_name='products',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product',
        related_query_name='products',
        null=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='product',
        related_query_name='products',
        null=True,
    )

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=3,
        default=A,
    )
    product = models.CharField(max_length=300)
    color = models.ManyToManyField(Color, blank=True)
    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        default=A,
    )

    price = models.IntegerField()
    description = models.TextField(null=True)
    is_new_collection = models.BooleanField(default=False)
    text1 = models.CharField(max_length=250, null=True, blank=True)
    text2 = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.product


class Images(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='image',
        related_query_name='images',
        null=True,
    )
    image = models.FileField(upload_to="product_images/", null=True, blank=True)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
