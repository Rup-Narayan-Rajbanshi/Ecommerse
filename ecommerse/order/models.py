import uuid
from django.conf import settings

from django.db import models
from django.utils.translation import gettext_lazy as _

from product.models import Product
# Create your models here.


class Order(models.Model):
    PENDING = 'PENDING'
    IN_TRANSIT = 'IN_TRANSIT'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = (
        (PENDING, "pending"),
        (IN_TRANSIT, "in_transit"),
        (COMPLETED, "completed"),
        (CANCELLED, "cancelled"),
    )

    total_price = models.BigIntegerField(verbose_name=_('Total Price'))
    order_code = models.UUIDField(
        primary_key=False,
        default=uuid.uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Order placed at"))
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='order',
        related_query_name='orders'
    )
    status = models.CharField(
        max_length=40,
        choices=STATUS_CHOICES,
        default=PENDING,
        verbose_name=_("Order status")
    )
    customer_name = models.CharField(max_length=250, blank=True, null=True)
    customer_address = models.CharField(max_length=250, blank=True, null=True)
    customer_ph_no = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.id)


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_order',
        null=True
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='product_order',
        null=True
    )
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    isbn = models.CharField(max_length=13, verbose_name=_('ISBN'))
    total_price = models.BigIntegerField(verbose_name=_('Total Price'))
    product_json = models.TextField(null=True, blank=True)
